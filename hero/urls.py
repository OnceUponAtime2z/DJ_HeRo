from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_HERO11/', views.list_HERO11, name='list_HERO11'),
    path('list_HERO12/', views.list_HERO12, name='list_HERO12'),
    path('list_HERO13/', views.list_HERO13, name='list_HERO13'),
    path('list_HERO14/', views.list_HERO14, name='list_HERO14'),
    path('list_HERO15/', views.list_HERO15, name='list_HERO15'),
    path('list_HERO16/', views.list_HERO16, name='list_HERO16'),
    path('list_HERO17/', views.list_HERO17, name='list_HERO17'),
    path('list_HERO18/', views.list_HERO18, name='list_HERO18'),
    path('list_HERO19/', views.list_HERO19, name='list_HERO19'),
    path('list_HERO20/', views.list_HERO20, name='list_HERO20'),
    path('Myherois/', views.Myherois, name='Myherois'),
]