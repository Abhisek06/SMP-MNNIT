from django.contrib import admin
from django.urls import path
from . import views

app_name = 'SMP'

# Pipeline for the website.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('clubs/', views.clubs, name = "clubs"),
    path('events/', views.events, name = "events"),
    path('sports/', views.sports, name = "sports"),
    path('academics/', views.academics, name = "academics"),
    path('campus_life/', views.campus_life, name = "campus_life"),
    path('extra_curricular/', views.extra_curricular, name = "extra_curricular"),
    path('FAQ/', views.FAQ, name = "FAQ"),
    path('login/', views.loginbase, name = "loginbase"),
    path('contacts/', views.contacts, name = "contacts"),
    path('details/', views.details, name = "details"), 
    path('details/<str:usn>/', views.profile, name = "profile"), 
    path('details/finalyear/<str:name>/', views.finalprofile, name = "profile4"), 
    path('resources/', views.resources, name = "resources"),
    path('Read_More/', views.readmore, name = "readmore"),
    path('Your_profile/', views.selfdetails, name = "selfdetails"),
    path('logout/', views.logout_request, name = "logout_request"),
    path('data_add/', views.run, name = "run"),

]