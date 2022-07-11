from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import URLModel


class LoginForm(AuthenticationForm):
    """Форма авторизации пользователя"""
    username = forms.CharField(label='Имя')
    password = forms.CharField(label='Пароль')


class RegisterForm(UserCreationForm):
    """Форма регистрации пользователя"""
    username = forms.CharField(label='Имя пользователя')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Подтверждение пароля')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class URLForm(forms.ModelForm):
    """Форма ввода url"""
    start_url = forms.URLField()


    class Meta:
        model = URLModel
        fields = ('start_url',)