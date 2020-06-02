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
        m2n = stu.mentor_name                                            # 2nd year mentor name
        m2reg = stu.mentor_regn                                          # 2nd year mentor registration number
        mentor2ndus = User.objects.get(username = m2reg)                  # 2nd year mentor from users
        mentor2nd = Student.objects.get(user = mentor2ndus)              # 2nd year mentor from students
        m3n = mentor2nd.mentor_name                                            # 3rd year mentor name
        m3reg = mentor2nd.mentor_regn                                          # 3rd year mentor registration number

        print(mentor2nd)
        print(stu)
        return render(request,"SMP/mentor1.html", {'mentor2' : m2n,'mentor2reg' : m2reg, 'student' : stu, 'mentor3' : m3n, 'mentor3reg' : m3reg})

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

def profile(request, usn):
    usnm = User.objects.get(username = usn)
    stud = Student.objects.get(user = usnm)
    ment = Mentor.objects.get(mentor = stud)
    roomno = ment.roomn
    contactno = ment.contactn
    hstl = ment.hostel
    fname = ment.mentor.user.first_name
    lname = ment.mentor.user.last_name
    year = ment.mentor.syear
    print(usn)
    return render(request, 'SMP/profile.html', {'username' : usn, 'room':roomno, 'contact':contactno, 'hostel':hstl, 'firstname':fname, 'lastname':lname, 'year':year})

