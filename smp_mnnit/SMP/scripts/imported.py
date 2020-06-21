import csv 
# from .models import Student, Mentor
from django.contrib.auth import login

def run():
    fhand = open('many/dat.csv')
    reader = csv.reader(fhand)


    for row in reader:
        print(row)
        # User.id() = row[0]
        post = User(username = row[1], password = row[2])

        # post.username() = row[1]
        # post.password() = row[2]
        post.first_name = row[3]
        post.last_name = row[4]

        post.save()