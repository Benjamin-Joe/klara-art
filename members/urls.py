from django.urls import path
from . import views

# Urls.py member's file

urlpatterns = [
    path('login_view', views.login_view, name="login"),
    path('logout_view', views.logout_view, name="logout"),
    path('register_view', views.register_view, name="register"),
    path('newsletter_view', views.newsletter_view, name="newsletter"),
]
