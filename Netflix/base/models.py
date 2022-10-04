import email
from email.policy import default
from pydoc import describe
from pydoc_data.topics import topics
from statistics import mode
from tkinter.tix import MAX
from turtle import up
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.forms import CharField, ModelForm
import uuid

# Create your models here.

Age_choices = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

Movie_genre = (
    ('Action', 'Action'),
    ('Animation', 'Animation'),
    ('Comedy', 'Comedy'),
    ('Crime', 'Crime'),
    ('Drama', 'Drama'),
    ('Experimental', 'Experimental'),
    ('Fantasy', 'Fantasy'),
    ('Historical', 'Historical'),
    ('Horror', 'Horror'),
    ('Romance', 'Romance'),
    ('Science Fiction', 'Science Fiction'),
    ('Thriller', 'Thriller'),
    ('Western', 'Western'),

)




class CustomUser(AbstractBaseUser):
    profiles = models.ManyToManyField('Profile', blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=False, max_length = 200)
    username = models.CharField(max_length = 20, null = True)
    age = models.CharField(max_length=20, choices=Age_choices)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return (self.name)

class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    cast = models.TextField(max_length=MAX, null=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    genre = models.CharField(max_length=20, choices=Movie_genre)
    videos = models.ManyToManyField('video')
    poster = models.ImageField(upload_to='flyers')
    age = models.CharField(max_length=10, choices=Age_choices)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return (self.title)

class Video(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='movies')
