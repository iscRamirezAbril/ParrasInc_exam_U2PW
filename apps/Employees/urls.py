from django.contrib import admin
from django.urls import path
from apps.Employees.views import *

urlpatterns = [
    # Por terminar #
    path('', index, name='index'),
    # Listo #
    path('login/', Employee_login, name = "emp_login"), # This is the path to the login.html file
    # Listo #
    path('register/', register, name = 'emp_register'), # This is the path to the signup.html file
    # Por modificar #
    path('profile/', index), # This is the path to the signup.html file
    # Listo #
    path('logout/', Emp_logout, name = 'emp_logout'), # This is the path to the signup.html file
    # Por trabajar (Solo Administradores) #
    path('list/', index), # This is the path to the signup.html file
    # MODIFICAR DISEÑO #
    path('welcomePage/', welcomePage, name = 'welcomePage'),
    # Listo #
    path('dashboard', dashboard, name = 'dashboard'), # This is the path to the signup.html file);
    
    # |===============| ADMINISTRACIÓN DE EMPLEADOS |===============| #
    # TRABAJANDO... #
    path('dashboard_Employees', dashboard_Employees, name = 'dashboard_Employees'),
    # LISTO #
    path('worker_List', worker_List, name = 'worker_List'),
    # TRABAJANDO... #
    path('worker_assistence', worker_Assistence , name = 'worker_assistence'),
]