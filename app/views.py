from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')


def form(request):
    return render(request, 'input_form.html')


def dashboard(request):
    return render(request, "dashboard.html")
