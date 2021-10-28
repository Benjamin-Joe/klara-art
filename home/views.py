from django.shortcuts import render


# Homepage view
def home_view(request):
    return render(request, 'home/home.html')
