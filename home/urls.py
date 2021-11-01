from django.contrib import admin
from django.urls import path
from . import views

# Urls.py home file

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
]