from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student, Mentor, FinalMentor
from django.contrib import messages
import csv
from django.contrib.auth.decorators import user_passes_test


def home(request):
    return render(request, "SMP/homepage.html")

def loginbase(request):
    if request.user.is_authenticated:
        return redirect("SMP:details")
    if request.method == "POST":
        uname = request.POST.get("reg_n", "")
        paswo = request.POST.get("passw", "")
        user = authenticate(username = uname, password = paswo)
        if user is not None:
            login(request, user)
            return redirect("SMP:home")
        else:
            messages.info(request, 'Invalid Credentials!')
            
            return redirect("SMP:loginbase")
    
    
    return render(request, "SMP/signin.html")

def contacts(request):
    return render(request, 'SMP/contact.html')

def events(request):
    return render(request, 'SMP/events.html')

def academics(request):
    return render(request, 'SMP/academics.html')

def campus_life(request):
    return render(request, 'SMP/infra.html')

def extra_curricular(request):
    return render(request, 'SMP/extra.html')

def FAQ(request):
    return render(request, 'SMP/faq.html')

def details(request):
    if request.user.is_authenticated:
        us = request.user
        stu = Student.objects.get(user = us)
        m2n = stu.mentor_name                                            # year+1 mentor name
        m2reg = stu.mentor_regn                                          # year+1 mentor registration number
        mentor2ndus = User.objects.get(username = m2reg)                  # year+1 mentor from users
        mentor2nd = Student.objects.get(user = mentor2ndus)              # year+1 mentor from students
        m3n = mentor2nd.mentor_name                                            # year+2 mentor name
        m3reg = mentor2nd.mentor_regn                                          # year+2 mentor registration number
        branchm = stu.branch
        year = stu.syear
        fment = FinalMentor.objects.filter(dept = branchm)
        return render(request,"SMP/mentor1.html", {'mentor2' : m2n,'mentor2reg' : m2reg, 'student' : stu, 'mentor3' : m3n, 'mentor3reg' : m3reg, 'mentor4': fment, 'year':year })

    else:
        return redirect("SMP:loginbase")

def clubs(request):
    return render(request,"SMP/clubs.html")

def resources(request):
    return render(request,"SMP/resources.html")

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
    return render(request, 'SMP/profile.html', {'username' : usn, 'room':roomno, 'contact':contactno, 'hostel':hstl, 'firstname':fname, 'lastname':lname, 'year':year})

def finalprofile(request, name):

    mentf = FinalMentor.objects.get(name = name)
    mentf_regn = mentf.regn
    mentf_roomn = mentf.roomn
    mentf_contact = mentf.contactn
    mentf_hostel = mentf.hostel
    mentf_dept = mentf.dept
    return render(request, 'SMP/profile4.html', {'username' : mentf_regn, 'room':mentf_roomn, 'contact':mentf_contact, 'hostel':mentf_hostel, 'name' : name, 'year': 'Final'})

def sports(request):
    return render(request, 'SMP/sports.html')

def selfdetails(request):
    usn = request.user
    usnm = User.objects.get(username = usn)
    stud = Student.objects.get(user = usnm)
    # ment = Mentor.objects.get(mentor = stud)
    # roomno = ment.roomn
    # contactno = ment.contactn
    # hstl = ment.hostel
    primarymentor = stud.mentor_name
    primarymentorusn = stud.mentor_regn
    fname = stud.user.first_name
    lname = stud.user.last_name
    year = stud.syear
    return render(request, 'SMP/profileself.html', {'username' : usn, 'pmentor':primarymentor,'pmentorusn':primarymentorusn, 'firstname':fname, 'lastname':lname, 'year':year})

@user_passes_test(lambda u: u.is_superuser)  
def run(request):
    fhand = open('SMP/scripts/many/dat.csv')
    reader = csv.reader(fhand)


    for row in reader:
        
        post, created = User.objects.get_or_create(username = row[1])

        post.set_password(row[2])
        post.first_name = row[3]
        post.last_name = row[4]

        post.save()
        print(post)
    
    return HttpResponse('data added')

    