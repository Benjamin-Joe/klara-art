from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
