from django.test import TestCase
from django.contrib.auth.models import User

from SoundCloudApp.models import Album, Song


class AlbumsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password='testing123')
        self.user.save()

    def _require_login(self):
        self.client.login(username='testuser', password='testing123')

    def create_ablum(self, artist="gemi", album_title="7ob gamd", genre="rock", album_logo="msh mohm"):
        return Album.objects.create(artist=artist, album_title=album_title,genre=genre, album_logo=album_logo)

    def test_album_creation(self):
        a = self.create_ablum()
        self.assertTrue(isinstance(a, Album))
        self.assertEqual(a.__str__(), a.album_title + '-' + a.artist)


class SongsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password='testing123')
        self.user.save()

    def _require_login(self):
        self.client.login(username='testuser', password='testing123')

    def create_song(self, album=Album.objects.get(pk=1), file_type="mp3", song_title="ma balash"):
        return Song.objects.create(album=album, file_type=file_type, song_title=song_title)

    def test_song_creation(self):
        s = self.create_song()
        self.assertTrue(isinstance(s, Song))
        self.assertEqual(s.__str__(), s.song_title)


