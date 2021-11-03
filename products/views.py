from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Products, Category
from django.db.models import Q


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
# Search bar view
# Category dropdown view
def products_view(request):
    products = Products.objects.all()

    category = request.GET.get('category')
    if category is None:
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category__name=category)
    categories = Category.objects.all()
   
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                print(request, "")
                return redirect(reverse('products'))
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    context = {
        'products': products,
        'search_term': query,
        'categories': categories
    }

    return render(request, 'products/products.html', context)
