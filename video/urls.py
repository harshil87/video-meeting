from django import urls
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.user_register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('meeting/',views.video_call,name="video_call"),
    path('join_room/',views.join_room,name="join_room"),
]
