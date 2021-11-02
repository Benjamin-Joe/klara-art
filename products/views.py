from django.shortcuts import render, get_object_or_404
from .models import Products, Category


# For for individual products
def product_detail(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    context = {
        'product': product,
        }
    return render(request, 'products/product_detail.html', context)


# Category view
def categories(request):
    return {
        'categories': Category.objects.all()
    }


# Products view
def products_view(request):
    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
