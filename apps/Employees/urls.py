from django.contrib import admin
from django.urls import path
from apps.Employees.views import *

urlpatterns = [
    # Por terminar #
    path('', index, name='index'),
    # Listo #
    path('login/', Employee_login, name = "emp_login"), # This is the path to the login.html file
    # Listo #
    path('register/', register), # This is the path to the signup.html file
    # Por modificar #
    path('profile/', index), # This is the path to the signup.html file
    # Listo #
    path('logout/', Emp_logout, name = 'emp_logout'), # This is the path to the signup.html file
    # Por trabajar (Solo Administradores) #
    path('list/', index), # This is the path to the signup.html file
    
    path('welcomePage/', welcomePage, name = 'welcomePage'),
    # Dashboard de administradores (Solo Administradores) #
    path('dashboard_admin/', dashboard_admin, name = 'dashboard_admin'), # This is the path to the signup.html file);
    # Dashboard de empleados #
    path('dashboard_employee/', dashboard_employee, name = 'dashboard_employee'), # This is the path to the signup.html file);

]