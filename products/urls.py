from django.urls import path
from . import views

# Urls.py products file

urlpatterns = [
    path('', views.products_view, name='products')
]