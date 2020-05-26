from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):                                        # for students

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    mentor_name = models.CharField(max_length = 30)
    branch = models.CharField(max_length = 40)
    syear = models.CharField(max_length = 10, default = "")         # year of student

    def __str__(self):
        return self.username

class Mentor(models.Model):                                         # for mentors

    name = models.CharField(max_length = 30)
    usname = models.CharField(max_length = 16)
    pasw = models.CharField(max_length = 16)
    dept = models.CharField(max_length = 40)
    myear = models.CharField(max_length = 10, default = "")         # year of mentor

    def __str__(self):
        return self.usname
