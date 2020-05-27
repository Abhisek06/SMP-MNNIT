from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student, Mentor


def home(request):
    return render(request, "SMP/homepage.html")

def loginbase(request):
    if request.method == "POST":
        uname = request.POST.get("reg_n", "")
        paswo = request.POST.get("passw", "")
        user = authenticate(username = uname, password = paswo)
        if user is not None:
            login(request, user)
            return redirect("SMP:home")
        else:
            return HttpResponse("ERROR")
    
    
    return render(request, "SMP/signin.html")

def about_us(request):
    return HttpResponse("Hello")

def general_info(request):
    return HttpResponse("Hello")

def academics(request):
    return HttpResponse("Hello")

def campus_life(request):
    return HttpResponse("Hello")

def extra_curricular(request):
    return HttpResponse("Hello")

def questions(request):
    return HttpResponse("Hello")

def details(request):
    return HttpResponse("Hello")

def departments(request):
    return HttpResponse("Hello")

def contacts(request):
    return HttpResponse("Hello")

def resources(request):
    return HttpResponse("Hello")

def infrastructure(request):
    return HttpResponse("Hello")

def logout_request(request):
    logout(request)
    return redirect("SMP:loginbase")

