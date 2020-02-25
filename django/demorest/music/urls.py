"""
Import packages
"""
from django.urls import path
from rest_framework import routers

from . import views


urlpatterns = [
    path('v1/musics', views.MusicView.as_view()),
    path('v1/musics/<str:id>',  views.MusicView.as_view())
]
