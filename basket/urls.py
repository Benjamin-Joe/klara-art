from django.contrib import admin
from django.urls import path
from . import views

# Urls.py home file

urlpatterns = [
    path('', views.basket_view, name='basket'),
    ]