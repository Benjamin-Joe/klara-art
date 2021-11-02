from django.shortcuts import render
from .models import Products, Category


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
