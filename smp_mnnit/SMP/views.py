from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student, Mentor
from django.contrib import messages


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
            # messages.error(request, 'Invalid Credentials!')
            return redirect("SMP:loginbase")
    
    
    return render(request, "SMP/signin.html")

def about_us(request):
    return HttpResponse("Hello")

def general_info(request):
    return HttpResponse("Hello")

def academics(request):
    return HttpResponse("Hello")

def campus_life(request):
    return render(request, 'SMP/infra.html')

def extra_curricular(request):
    return HttpResponse("Hello")

def FAQ(request):
    return HttpResponse("Hello")

def details(request):
    if request.user.is_authenticated:
        us = request.user
        stu = Student.objects.get(user = us)
        mn = stu.mentor_name
        print(mn)
        print(stu)
        return render(request,"SMP/mentor1.html", {'mentor2' : mn , 'student' : stu})

    else:
        return redirect("SMP:loginbase")

def contacts(request):
    return HttpResponse("Hello")

def resources(request):
    return HttpResponse("Hello")

def logout_request(request):
    logout(request)
    return redirect("SMP:loginbase")
    
def readmore(request):
    return render(request, 'SMP/readMore.html')

