from datetime import datetime
from django.db import models

class Video(models.Model):
    video_file = models.FileField(upload_to='videos_uploaded', null=True)
    date_uploaded = models.DateField(default=datetime.now)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
