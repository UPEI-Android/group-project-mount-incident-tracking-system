from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.WARNING, 'Invalid Credentials')
            return render(request, 'index.html')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'index.html')


def form(request):
    if request.user.is_authenticated:
        return render(request, 'input_form.html',
                      {"first_name": request.user.first_name, "last_name": request.user.last_name})
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
    else:
        messages.error(request, f'User is not authenticated')
        return redirect('home')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'User Successfully Logged Out')
    else:
        messages.add_message(request, messages.WARNING, 'No User Authenticated')
    return redirect('home')
