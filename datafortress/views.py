import os
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from .forms import UserRegistrationForm, VideoForm, NotificationForm
from django.contrib.auth import login, authenticate
from .models import Video, Notification
from django.contrib.auth.decorators import user_passes_test, login_required
from django.conf import settings
from .whatsapp_utils import send_whatsapp_message

def index(request):
    return render(request , 'index.html')

def user_in_editor(user):
    return user.groups.filter(name='editor').exists()

def user_in_creator(user):
    return user.groups.filter(name='creator').exists()



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='editor').exists():
                return redirect('welcome_editor')
            elif user.groups.filter(name='creator').exists():
                return redirect('welcome_creator')
        else:
                messages.info(request, "Invalid Credentials")
                return redirect('login_user')
    return render(request, 'login_user.html')


@user_passes_test(user_in_editor)
def welcome_editor(request):
    return render(request, 'welcome_editor.html')


@user_passes_test(user_in_creator)
def welcome_creator(request):
    return render(request, 'welcome_creator.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['role']
            u = form.cleaned_data['username']
            e = form.cleaned_data['email']
            if User.objects.filter(email = e).exists():
                messages.info(request , "Email Already in use.")
                return redirect('signup')
            elif User.objects.filter(username = u).exists():
                messages.info(request , "Username Already in use.")
                return redirect('signup')
            else:
                form.save()
            if x == 'editor' or x == 'Editor':
                    user = User.objects.get(username = u)
                    group = Group.objects.get(name = "editor")
                    user.groups.add(group)
            elif x == 'creator' or x == 'Creator':
                user = User.objects.get(username = u)
                group = Group.objects.get(name = "creator")
                user.groups.add(group)
            return redirect('success')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})


def success(request):
    return render(request , 'success.html')

@user_passes_test(user_in_editor)
@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                video = form.save(commit=False)
                video.uploader = request.user
                video.save()
                messages.info(request , "Video Uploaded Successfully.")
            except Exception as e:
                error_message = f"An error occurred during file upload: {str(e)}"
                return render(request, 'upload_error.html', {'error_message': error_message})
        else:
            error_message = "Form is not valid. Please check your inputs."
            return render(request, 'upload_error.html', {'error_message': error_message})
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

@user_passes_test(user_in_editor)
@login_required
def notification_send(request):
    if request.method == 'POST':
        notif_form = NotificationForm(request.user, request.POST)
        if notif_form.is_valid():
            try:
                notification = notif_form.save(commit=False)
                notification.sender = request.user
                to_number = notif_form.cleaned_data['phone']
                new_message = notif_form.cleaned_data['message']
                message = f"New Message: {new_message}"                
                success, error_message = send_whatsapp_message(to_number, message)
                notification.save()
                if success:
                    messages.info(request , "Notification Sent Successfully.")
                    return redirect('notification_send')
                else:
                    messages.info(request, "Error sending WhatsApp notification.")
                    return redirect('notification_send')
            except Exception as e:
                    error_message = f"An error occurred during sending notification: {str(e)}"
                    return render(request, 'notification_send.html', {'error_message': error_message})
        else:
            error_message = "Form is not valid. Please check your inputs."
            return render(request, 'notification_send.html', {'error_message': error_message})
    else:
        notif_form = NotificationForm(request.user)
    return render(request, 'notification_send.html', {'notif_form' : notif_form})


@user_passes_test(user_in_editor)
@login_required
def video_list_editor(request):
    videos = Video.objects.filter(uploader=request.user)
    return render(request, 'video_list_editor.html', {'videos':videos})

@user_passes_test(user_in_creator)
@login_required
def video_list_creator(request):
    videos = Video.objects.filter(receiver=request.user)
    return render(request, 'video_list_creator.html', {'videos':videos})


@login_required
def delete_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    video_path = os.path.join(settings.MEDIA_ROOT, str(Video.video_file))
    if request.method == 'POST':
        video.delete()
    if os.path.exists(video_path):
        os.remove(video_path)
    return redirect('video_list_editor')


@login_required
def approve_video(request, video_id):
    return redirect('video_list_creator')


@login_required
def notification_list(request):
    # Retrieve notifications for the current user (creator)
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'notification_list.html', {'notifications': notifications})


@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    if notification.recipient == request.user:
        notification.delete()
    return redirect('notification_list')

