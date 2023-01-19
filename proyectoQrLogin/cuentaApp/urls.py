from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]