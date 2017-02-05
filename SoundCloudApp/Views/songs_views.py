from django.views import generic
from django.views.generic.edit import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from braces.views import LoginRequiredMixin

from SoundCloudApp.models import Album, Song
from SoundCloudApp.forms import SongForm


class SongView(LoginRequiredMixin, generic.ListView):
    template_name = 'SoundCloudApp/index.html'
    context_object_name = 'songs'
    login_url = '/'

    def get_queryset(self):
        return Song.objects.all()


class SongCreate(LoginRequiredMixin, View):
    form_class = SongForm
    template_name = 'SoundCloudApp/song_form.html'
    login_url = '/'

    def get(self, request, pk):
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request , pk):
        form = self.form_class(request.POST)

        if form.is_valid():
            song = form.save(commit=False)
            album = Album.objects.get(pk=pk)
            song.album = album
            song.song_title = request.POST['song_title']
            album.file_type = request.POST['file_type']
            song.save()
            return redirect('/albums/'+str(pk))
        return render(request, self.template_name, {'form': form})


class SongDelete(LoginRequiredMixin, View):
    login_url = '/'

    def post(self, request, pk):
        song = Song.objects.get(pk=pk)
        album_id = song.album_id
        song.delete()
        return redirect('/albums/'+str(album_id))


class SongFavourite(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        u = User.objects.get(username=request.user)
        if u.song_likes.filter(pk=song.id):
            song.song_likes.remove(request.user)
        else:
            song.song_likes.add(request.user)
        song.save()
        return redirect('SoundCloudApp:index')
