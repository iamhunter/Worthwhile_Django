from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django import forms



# Create your models here.
DURATION_CHOICES = (
    ('2', '2'),
    ('8', '8')
)

class Course(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField(max_length = 500)
    Instructor = models.CharField(max_length = 100)
    Duration = models.CharField(max_length = 1, choices = DURATION_CHOICES, default = '2')
    CourseArt = models.ImageField()
    
class Course_index(ModelForm):
    class Meta:
        model = Course
        fields = ['Title', 'Description', 'Instructor', 'Duration', 'CourseArt']
        widgets = {
            'Title': forms.TextInput(attrs={'placeholder': 'Name it something good'}),
            'Description': forms.TextInput(attrs={'placeholder': 'Provide some information about what students will learn'}),
            'Instructor': forms.TextInput(attrs={'placeholder': 'Django Guru'}),


        }
