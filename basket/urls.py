from django.urls import path
from . import views

# Urls.py home file

urlpatterns = [
    path('', views.basket_view, name='basket'),
    path('add/<product_id>', views.add_to_basket, name='add_to_basket'),
    ]
