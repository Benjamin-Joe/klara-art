from django.shortcuts import render
from .forms import Contact_Form

# Homepage view
def home_view(request):
    return render(request, 'home/home.html')


# Contact view
def contact_view(request):
    form = Contact_Form()
    context = {
        'form': form
        }

    return render(request, 'contact/contact.html', context)


# About view
def about_view(request):
    return render(request, 'about/about.html')


