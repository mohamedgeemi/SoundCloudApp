from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Album, Song


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('artist', 'album_title', 'genre', 'album_logo', 'album_likes')


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('album', 'song_title', 'file_type')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email = validated_data["email"],
            username = validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
