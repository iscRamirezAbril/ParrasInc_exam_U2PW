from django.contrib import admin
from django.urls import path
from apps.Employees.views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', Employee_login, name = "emp_login"), # This is the path to the login.html file
    path('register/', register), # This is the path to the signup.html file
    path('profile/', index), # This is the path to the signup.html file
    path('logout/', Emp_logout, name = 'emp_logout'), # This is the path to the signup.html file
    path('list/', index), # This is the path to the signup.html file
]