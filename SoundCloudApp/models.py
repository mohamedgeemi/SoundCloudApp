from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    album_likes = models.ManyToManyField(User, related_name='album_likes', blank=True)

    def __str__(self):
        return self.album_title + '-' + self.artist

    def get_absolute_url(self):
        return reverse('SoundCloudApp:detail', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=200)
    song_title = models.CharField(max_length=300 , default="")
    song_likes = models.ManyToManyField(User, related_name='song_likes', blank=True)

    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('SoundCloudApp:detail', kwargs={'pk': self.album_id})




