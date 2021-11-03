from django.shortcuts import render


# Homepage view
def basket_view(request):
    return render(request, 'basket/basket.html')

