from django.views import generic
from django.views.generic.edit import UpdateView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from braces.views import LoginRequiredMixin

from SoundCloudApp.models import Album
from SoundCloudApp.forms import AlbumForm


class AlbumIndex(LoginRequiredMixin, generic.ListView):
    template_name = 'SoundCloudApp/index.html'
    context_object_name = 'all_albums'
    login_url = '/'

    def get_queryset(self):
        return Album.objects.all()


class AlbumCreate(LoginRequiredMixin, View):
    form_class = AlbumForm
    template_name = 'SoundCloudApp/album_form.html'
    login_url = '/'

    def get(self, request):
            form = self.form_class(None)
            return render(request, self.template_name , {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.artist = request.POST['artist']
            album.album_title = request.POST['album_title']
            album.genre = request.POST['genre']
            album.album_logo = request.POST['album_logo']
            album.save()
            return redirect('SoundCloudApp:index')
        return render(request, self.template_name, {'form': form})


class AlbumDetail(LoginRequiredMixin, generic.DetailView):
    model = Album
    template_name = 'SoundCloudApp/detail.html'
    login_url = '/'


class AlbumUpdate(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    login_url = '/'


class AlbumDelete(LoginRequiredMixin, View):
    login_url = '/'

    def post(self, request, pk):
        album = Album.objects.get(pk=pk)
        album.delete()
        return redirect('SoundCloudApp:index')


class AlbumFavourite(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        u = User.objects.get(username=request.user)
        if u.album_likes.filter(pk=album.id):
            album.album_likes.remove(request.user)
        else:
            album.album_likes.add(request.user)
        album.save()
        return redirect('SoundCloudApp:index')