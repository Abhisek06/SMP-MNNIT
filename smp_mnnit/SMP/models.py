from django.db import models
from django.contrib.auth.models import User

def get_image_path(instance, filename):
     return 'images/{0}/{1}'.format(instance.username, filename)     # define image upload path

# Create your models here.

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
