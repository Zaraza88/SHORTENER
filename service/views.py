import pyshorteners

from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import URLModel
from .forms import LoginForm, RegisterForm, URLForm

#Для упрощенной навигации я решил не распихивать все по разным файлам, т.к кода не много. 
def view_info(request):
    """Вывод информации о ссылках юзера"""
    user = request.user
    url = URLModel.objects.filter(user=user)
    context = {'url': url, 'user': user}
    return render(request, 'service/list_url.html', context=context)


def shorten_url(data):
    """Укорачиваем ссылки"""
    url = pyshorteners.Shortener().tinyurl.short(data)
    return url


def index(request):
    """Получаем url и сохраняем в бд"""
    if request.user.is_authenticated:
        if request.method == "POST":
            form = URLForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data.get('start_url')
                modified_url = shorten_url(data)
                update_model = URLModel(user=request.user, start_url=data, modified_url=modified_url)
                update_model.save()
                messages.info(request, f'Ваша сокращенная ссылка - {update_model.modified_url}')
                return redirect('index')
            else:
                messages.error(request, 'Неккоректный url')
    else:
        messages.error(request, 'Зарегистрируйся или авторизуйся для того что бы пользоваться сервисом')
    return render(request, 'service/index.html')


def register(request):
    """Регистрация"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'service/register.html')


def user_login(request):
    """Вход в аккаунт"""
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'service/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
