from django.urls import path 
from . import views

urlpatterns=[
    path('', views.detect, name='detectarQr'),
    path('camera_feed', views.camera_feed, name='camera_feed'),
]