from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Login_view code lines 7 -17 taken from django website, make note
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.success(request, "Username/Password Incorrect, Try Again")
            return redirect('login')

    else:
        return render(request, 'authentication/login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, "You Are Logged Out")
    return redirect('login')


# Code snipit from codemy https://www.youtube.com/watch?v=EqjRhO5CK6A&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=24
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Account Registered"))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {
            'form': form,
        })
