import os
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from .forms import VideoForm
from .models import Video
from django.contrib.auth.decorators import user_passes_test



def index(request):
    return render(request , 'index.html')

def user_in_editor(user):
    return user.groups.filter(name='editor').exists()


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
            messages.info(request , "Invalid Credentials")
            return redirect(request , 'login_user')
    return render(request, 'login_user.html')

def welcome_editor(request):
    return render(request, 'welcome_editor.html')

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
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('video_list')
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
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos':videos})


def delete_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    if request.method == 'POST':
        video.delete()
    return redirect('video_list')

