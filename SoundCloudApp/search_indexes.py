from haystack import indexes

from .models import Album, Song


class AlbumIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    artist = indexes.CharField(model_attr='artist')
    album_title = indexes.CharField(model_attr='album_title')
    genre = indexes.CharField(model_attr='genre')
    album_logo = indexes.CharField(model_attr='album_logo')
    is_favorite = indexes.BooleanField(model_attr='is_favorite')

    def get_model(self):
        return Album


class SongIndex(indexes.SearchField, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    song_title = indexes.CharField(model_attr='song_title')
    file_type = indexes.CharField(model_attr='file_type')
    is_favorite = indexes.BooleanField(model_attr='is_favorite')

    def get_model(selfs):
        return Song




