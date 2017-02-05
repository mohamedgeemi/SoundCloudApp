from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from SoundCloudApp.models import Album, Song
from accounts.forms import UserForm


class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', email='test@gmail.com', password='testing123')
        self.user.save()

    def create_user(self, first_name='Gemi', last_name='Mohamed', username='testuser3', email='test@gmail.com', password='testing123'):
        return User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)

    def _require_login(self):
        self.client.login(username='testuser2', password='testing123')

    def test_user_form_view(self):
        resp = self.client.get("/register/")
        self.assertEqual(resp.status_code, 200)
        context = {'first_name': 'gemi',
                   'last_name': 'gemgem',
                   'username': 'gems',
                   'password': '4651',
                   'email':'gemi@gmgm.com'}
        resp = self.client.post("/register/", context)
        self.assertEqual(resp.status_code, 302)

    def test_login_form_view(self):
        user = self.create_user()
        user.save()
        url = reverse("accounts:login")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        context = {'username': user.username,
                   'password': user.password}
        resp = self.client.post(url, context)
        self.assertEqual(resp.status_code, 200)

    def test_userForm_invalid_form(self):
        a = self.create_user()
        context = {'first_name': a.first_name,
                   'last_name': '',
                   'username': a.username,
                   'password': a.password,
                   'email': a.email}
        form = UserForm(context)
        self.assertFalse(form.is_valid())

    def test_userForm_valid_form(self):

        context = {'first_name': 'ggg',
                   'last_name': 'mmm',
                   'username': 'omnia',
                   'password': 'testing123',
                   'email': 'a@shs.com'}
        form = UserForm(context)
        self.assertTrue(form.is_valid())
