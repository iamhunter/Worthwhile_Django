from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


# Create your models here.
DURATION_CHOICES = (
    ('8', '8'),
    ('12', '12')
)

class Course(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField(max_length = 500)
    Instructor = models.CharField(max_length = 100)
    Duration = models.CharField(max_length = 2, choices = DURATION_CHOICES, default = '8')
    CourseArt = models.FileField(upload_to='uploads/')