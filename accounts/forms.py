from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password']