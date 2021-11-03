from decimal import Decimal
from django.conf import settings


# Code taken from boutique ado walkthrough project
def basket_contents(request):

    basket_items = []
    total = 0
    product_number = 0
    delivery = 4.99
    grand_total = total + delivery
  
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_number': product_number,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    return context
