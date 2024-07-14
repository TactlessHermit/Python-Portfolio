from django.db import models
from django.urls import reverse


# Create your models here.
class Designs(models.Model):
    name = models.TextField(max_length=255)
    software = models.TextField(max_length=255)
    description = models.TextField(max_length=1000, default='The fruits of my hobbies')
    #design_image = models.ImageField

    # After a new project is created, this calls detail.view
    def get_absolute_url(self):
        return reverse('designs:design_page', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + ", made using: " + self.software