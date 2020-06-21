from django.db import models
from django.contrib.auth.models import User
# from . import imported

def get_image_path(instance, filename):
     return 'images/{0}/{1}'.format(instance.username, filename)     # define image upload path

# Create your models here.
# class User(models.Model):                                        # for students

#     username = models.CharField(max_length = 20,default = "")
#     password = models.PasswordField(max_length = 30, default = "")
#     first_name = models.CharField(default = "", max_length = 20)
#     last_name= models.CharField(max_length = 20, default = "")
#     email = models.CharField(max_length = 50, default = "")         # year of student

#     def __str__(self):
#         return self.user.username

class Student(models.Model):                                        # for students

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    mentor_name = models.CharField(max_length = 30)
    mentor_regn = models.CharField(default = "", max_length = 10)
    branch = models.CharField(max_length = 40)
    syear = models.CharField(max_length = 10, default = "")         # year of student

    def __str__(self):
        return self.user.username

class Mentor(models.Model):                                         # for mentors

    mentor = models.OneToOneField(Student, models.CASCADE, default = "")
    roomn = models.CharField(max_length = 7, default = "")
    hostel = models.CharField(max_length = 40, default = "")
    contactn = models.CharField(max_length = 15, default = "")

    def __str__(self):
        return self.mentor.user.username

class FinalMentor(models.Model):                                         # for mentors

    regn = models.CharField(max_length = 16)
    dept = models.CharField(max_length = 40)
    roomn = models.CharField(max_length = 7, default = "")
    hostel = models.CharField(max_length = 40, default = "")
    contactn = models.CharField(max_length = 15, default = "")
    name = models.CharField(max_length = 40, default = "")
    def __str__(self):
        return self.name
