from django.urls import path
from . import views

# Urls.py products file

urlpatterns = [
    path('', views.products_view, name='products'),
    path('<product_id>', views.product_detail, name='product_detail')
]