from django.db import models
from django.urls import reverse


# Django creates a UID column in the background as the PK.
class Video(models.Model):
    title = models.TextField(max_length=250)
    genre = models.TextField(max_length=250)
    video_link = models.URLField(max_length=2000)

    # After a new video object is created, this calls detail.view
    def get_absolute_url(self):
        return reverse('videos:detail', kwargs={'pk': self.pk})

    # String representation of object (necessary for admin CRUD clarity)
    def __str__(self):
        return self.title + '-' + self.genre
