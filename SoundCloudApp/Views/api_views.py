from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import generics

from SoundCloudApp.models import Album, Song
from SoundCloudApp.serializers import UserSerializer, AlbumSerializer, SongSerializer
from SoundCloudApp.permissions import IsOwnerOrReadOnly


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ()
    authentication_classes = ()


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class AlbumList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AlbumCreate(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AlbumDetail(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AlbumUpdate(generics.UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class AlbumDelete(generics.DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class SongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SongCreate(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class SongDelete(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
