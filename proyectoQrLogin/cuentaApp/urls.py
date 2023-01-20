from django.urls import path
from django.views.generic import TemplateView

from . import views

#urls para que la pagina primera de cargar sea el template de login
#y luego redireccione al template home
urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]