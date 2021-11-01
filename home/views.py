from django.shortcuts import render


# Homepage view
def home_view(request):
    return render(request, 'home/home.html')


# Contact view
def contact_view(request):
    return render(request, 'contact/contact.html')


# About view
def about_view(request):
    return render(request, 'about/about.html')


