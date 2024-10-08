from django.db import models
from django.contrib.auth.models import User

def video_file_path(instance, filename):
    # Modify the upload path based on the receiver's username
    return f'media/{instance.receiver.username}/{filename}'

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    video_file = models.FileField(upload_to=video_file_path)
    is_public = models.CharField(max_length=20)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_videos', null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_videos', null=True)
    def __str__(self):
        return self.name + ": " + str(self.videofile)
    

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_sent')
    recipient = models.ForeignKey(User, related_name='received_notifications', on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15, default='')
    is_read = models.BooleanField(default=False)
    
    def mark_as_read(self):
        self.is_read = True
        self.save()