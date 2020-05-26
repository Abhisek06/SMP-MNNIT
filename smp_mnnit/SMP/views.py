from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def home(request):
    return HttpResponse("Hello")

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

def login(request):
    return HttpResponse("Hello")

def details(request):
    return HttpResponse("Hello")

def departments(request):
    return HttpResponse("Hello")

def contacts(request):
    return HttpResponse("Hello")

def resources(request):
    return HttpResponse("Hello")
