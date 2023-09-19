from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='media/')
    is_public = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name + ": " + str(self.videofile)