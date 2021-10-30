from django.shortcuts import render
from .models import Products


# Products view
def products_view(request):
    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
