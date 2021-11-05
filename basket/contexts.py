from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Products


# Code taken from boutique ado walkthrough project
def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery = 0

    basket = request.session.get('basket', {})

    for product_id, quantity in basket.items():
        product = get_object_or_404(Products, pk=product_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })
        grand_total = total + delivery
  
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    return context
