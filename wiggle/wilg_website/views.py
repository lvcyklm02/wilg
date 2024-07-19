from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def house(request):
    return render(request, "pages/house.html")

def rush(request):
    return render(request, "pages/rush.html")

def alumnae(request):
    return render(request, "pages/alumnae.html")

def summer(request):
    return render(request, "pages/summer.html")

def login(request):
    return render(request, "pages/login.html")