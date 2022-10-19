from django.contrib import admin
from django.urls import path
from apps.Employees.views import *

urlpatterns = [
    # PENDIENTE.... #
    path('', index, name='index'),
    # LISTO #
    path('login/', Employee_login, name = "emp_login"), # This is the path to the login.html file
    # LISTO #
    path('register/', register, name = 'emp_register'), # This is the path to the signup.html file
    # LISTO #
    path('logout/', Emp_logout, name = 'emp_logout'), # This is the path to the signup.html file
    # # Por trabajar (Solo Administradores) #
    # path('list/', index), # This is the path to the signup.html file
    # LISTO #
    path('welcomePage/', welcomePage, name = 'welcomePage'),
    # PENDIENTE... #
    path('dashboard/', dashboard, name = 'dashboard'), # This is the path to the signup.html file);
    
    # |===============| ADMINISTRACIÓN DE EMPLEADOS |===============| #
    # TRABAJANDO... #
    # Menú de administración de empleados #
    path('dashboard_Employees/', dashboard_Employees, name = 'dashboard_Employees'),
    # LISTO #
    # Lista de empleados con sus horarios correspondientes #
    path('worker_List/', worker_List, name = 'worker_List'),
    # LISTO #
    # Lista de asistencias de empleados por semana #
    path('worker_assistence/', ClockSystemReport, name = 'worker_assistence'),
]