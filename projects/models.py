from django.db import models
from django.urls import reverse


# Django creates a UID column in the background as the PK.
class Projects(models.Model):
    project_name = models.TextField(max_length=250)
    language = models.TextField(max_length=250)
    framework = models.TextField(max_length=250)
    description = models.TextField(max_length=2000)
    project_link = models.URLField(max_length=2000, default="https://github.com/TactlessHermit?tab=repositories")

    # After a new project is created, this calls detail.view
    def get_absolute_url(self):
        return reverse('projects:project-page', kwargs={'pk': self.pk})

    # String representation of object (necessary for admin CRUD clarity)
    def __str__(self):
        return self.project_name + '-' + self.language
