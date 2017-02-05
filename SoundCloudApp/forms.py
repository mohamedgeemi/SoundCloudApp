from django.contrib.auth.models import User
from django import forms

from .models import Album, Song


class AlbumForm(forms.ModelForm):
    artist = forms.CharField(required=True)
    album_title = forms.CharField(required=True)
    album_logo = forms.CharField(required=True)

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):
    song_title = forms.CharField(required=True)

    class Meta:
        model = Song
        fields = ['song_title', 'file_type']