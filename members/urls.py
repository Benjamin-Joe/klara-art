from django.urls import path
from . import views

# Urls.py member's file

urlpatterns = [
    path('login_view', views.login_view, name="login"),
]