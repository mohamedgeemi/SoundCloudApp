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
        return Album.objects.create(artist=artist, album_title=album_title, genre=genre, album_logo=album_logo)

    def test_album_list_view_noCredit(self):
        resp = self.client.get("/albums/")
        self.assertEqual(resp.status_code, 302)

    def test_album_list_view_withCredit(self):
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get("/albums/")
        self.assertEqual(resp.status_code, 200)

    def test_album_detail_view_noCredit(self):
        a = self.create_ablum()
        resp = self.client.get('/albums/' + str(a.id)+'/')
        self.assertEqual(resp.status_code, 302)

    def test_album_detail_view_withCredit(self):
        a = self.create_ablum()
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get('/albums/' + str(a.id) + '/')
        self.assertEqual(resp.status_code, 200)

    def test_album_create_noCredit(self):
        resp = self.client.get("/album/add/")
        self.assertEqual(resp.status_code, 302) #redirect check

    def test_album_create_withCredit(self):
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get("/album/add/")
        self.assertEqual(resp.status_code, 200)
        context= {'artist': 'gemi',
                  'album_title': 'el 7ob el 7ob',
                  'genre': 'jaaz',
                  'album_logo': 'mafesh'}
        resp = self.client.post("/album/add/", context)
        self.assertEqual(resp.status_code, 302)

    def test_album_update_noCredit(self):
        a = self.create_ablum()
        resp = self.client.get("/album/"+str(a.id)+"/update/")
        self.assertEqual(resp.status_code, 302) #redirect check

    def test_album_update_withCredit(self):
        a = self.create_ablum()
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get("/album/" + str(a.id) + "/update/")
        self.assertEqual(resp.status_code, 200)
        context= {'artist': 'gemi',
                  'album_title': 'el 7ob el 7ob',
                  'genre': 'jaaz',
                  'album_logo': 'mafesh'}
        resp = self.client.put("/album/" + str(a.id) + "/update/", context)
        self.assertEqual(resp.status_code, 200)

    def test_album_delete_noCredit(self):
        a = self.create_ablum()
        resp = self.client.post("album/"+str(a.id)+"/delete/")
        self.assertEqual(resp.status_code, 404) #redirect check

    def test_album_delete_withCredit(self):
        a = self.create_ablum()
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get("album/" + str(a.id) + "/delete/")
        self.assertEqual(resp.status_code, 404)

    def test_album_fav_noCredit(self):
        a = self.create_ablum()
        resp = self.client.put("/album/" + str(a.id) + "/fav/")
        self.assertEqual(resp.status_code, 302)

    def test_album_fav_withCredit(self):
        a = self.create_ablum()
        u = User.objects.get(username=self.user.username)
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get("/album/"+str(a.id)+"/fav/")
        self.assertEqual(u.album_likes.filter(pk=a.id).exists(), True)
        self.assertEqual(resp.status_code, 302)

    def test_search_noCredit(self):
        a = self.create_ablum()
        resp = self.client.get("/search/")
        self.assertEqual(resp.status_code, 302)

    def test_search_withCredit(self):
        a = self.create_ablum()
        q1 = a.album_title
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get("/search/?q=" + q1)
        self.assertEqual(resp.status_code, 200)


class SongsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password='testing123')
        self.user.save()

    def _require_login(self):
        self.client.login(username='testuser', password='testing123')

    def create_ablum(self, artist="gemi", album_title="7ob gamd", genre="rock", album_logo="msh mohm",
                     is_favorite=False):
        return Album.objects.create(artist=artist, album_title=album_title, genre=genre, album_logo=album_logo)


    def create_song(self, album=Album.objects.get(pk=1), file_type="mp3", song_title="ma balash"):
        return Song.objects.create(album=album, file_type=file_type, song_title=song_title)


    def test_song_list_view_noCredit(self):
        resp = self.client.get("/songs/")
        self.assertEqual(resp.status_code, 302)

    def test_song_list_view_withCredit(self):
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get("/songs/")
        self.assertEqual(resp.status_code, 200)

    def test_song_create_noCredit(self):
        a = self.create_ablum()
        resp = self.client.get("/album/" + str(a.id)+"/song/add/")
        self.assertEqual(resp.status_code, 302) #redirect check

    def test_song_create_withCredit(self):
        a = self.create_ablum()
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get("/album/" + str(a.id)+"/song/add/")
        self.assertEqual(resp.status_code, 200)
        context= {'album': a,
                  'file_type': 'mp3',
                  'song_title': 'hwa e7na 7abena?'}
        resp = self.client.post("/album/"+ str(a.id)+"/song/add/", context)
        self.assertEqual(resp.status_code, 302)

    def test_song_delete_noCredit(self):
        s = self.create_song()
        resp = self.client.get("song/"+str(s.id)+"/delete/")
        self.assertEqual(resp.status_code, 404) #redirect check

    def test_song_delete_withCredit(self):
        s = self.create_song()
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get("song/" + str(s.id) + "/delete/")
        self.assertEqual(resp.status_code, 404)

    def test_song_fav_noCredit(self):
        s = self.create_song()
        resp = self.client.get("/song/" + str(s.id) + "/fav/")
        self.assertEqual(resp.status_code, 302)

    def test_song_fav_withCredit(self): #fail
        s = self.create_song()
        u = User.objects.get(username=self.user.username)
        self._require_login()
        print(self.user.is_authenticated())
        resp = self.client.get("/song/"+str(s.id)+"/fav/")
        self.assertEqual(u.song_likes.filter(pk=s.id).exists(), True)
        self.assertEqual(resp.status_code, 302)










