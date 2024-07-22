from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Exec, Member


def home(request):
    return render(request, "pages/home.html")

def about(request):
    members = Member.objects.all()
    execs = list(Exec)

    positions = dict()

    for member in members:
        try:
            positions[member.exec_position].add(member.id)    
        except KeyError:
            print("How is there a key error on a defaultdict?")
            positions[member.exec_position] = set()
            positions[member.exec_position].add(member.id)

    print("positions are:", positions)
    return render(request, "pages/about.html", {"execs": execs, "members": members, "positions": positions})

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