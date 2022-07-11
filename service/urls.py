from django.urls import path

from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.view_info, name='list'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]