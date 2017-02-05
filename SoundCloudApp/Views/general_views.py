from django.views import generic
from django.views.generic.edit import View
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User

from braces.views import LoginRequiredMixin

from SoundCloudApp.models import Album, Song


class FavouritesView(LoginRequiredMixin, View):
    template_name = 'SoundCloudApp/index.html'
    login_url = '/'

    def get(self, request):
        u = User.objects.get(username=request.user)
        albums = u.album_likes.all()
        songs = u.song_likes.all()
        context = {'all_albums': albums,
                   'songs': songs}
        return render(request, self.template_name, context)


class Search(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request):
        albums = Album.objects.all()
        song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
            song_results = song_results.filter(
                Q(song_title__icontains=query)
            ).distinct()
            return render(request, 'SoundCloudApp/index.html', {
                'all_albums': albums,
                'songs': song_results,
            })
        else:
            return redirect('SoundCloud:index')

