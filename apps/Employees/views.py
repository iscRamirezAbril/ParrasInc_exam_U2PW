from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect


from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout


from datetime import date
from datetime import date

# |==========| DECORADORES |==========| #
from django.contrib.auth.decorators import *
from apps.Employees.decorators import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

# @unauthenticated_user
def Employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            text = 'Welcome back ' + request.user.employee.empFirstName
            messages.success(request, text)
            return redirect('welcomePage')

        else:
            messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = employeeForm()

    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            
            group, created  = Group.objects.get_or_create(name ='employee')
            user.groups.add(group)
            
            Employee.objects.create(
                empUsername = user,
                empEmail =     user.username,
                empFirstName = user.first_name,
                empLastName =  user.last_name,
            )
            
            text = 'Please, sign in'
            messages.success(request, text)
            
    context = {'form': form}
    return render(request, 'register.html', context)


# Función para cerrar sesión
def Emp_logout(request):
    logout(request)
    return redirect('emp_login')


# Página de inicio
#@login_required(login_url='emp_login')
def welcomePage(request):
    return render(request, 'Employees/welcomePage.html')


# Para acceder a esta página, se necesita estar logueado
#@login_required(login_url='emp_login')
def dashboard(request):
    return render(request, 'Employees/dashboard.html')

#@login_required(login_url='emp_login')
# @admin_only
def dashboard_Employees(request):
    return render(request, 'Employees/dashEmployees.html')


def employee_List(request):
    context = {'employee_List': Employee.objects.all()} # Se crea un diccionario con la lista de los empleados
    return render(request, 'Employees/employee_List.html', context)


# REPORTE DE ASISTENCIA DE TRABAJADORES #
#@login_required(login_url='emp_login')
def worker_List(request):
    context = {'worker_List': Worker.objects.all()}
    return render(request, 'Employees/worker_List.html', context)

current_week = date.today().isocalendar()[1] 

# REPORTE DE ASISTENCIA DEL TRABAJADOR ACTUAL #
def worker_Assistence(request):
    worker_Assistence = Assistence.objects.filter(assistDate__week=current_week).filter(assistWorker = request.user.pk)
    monday=False
    tuesday=False
    wednesday=False
    thursday=False
    friday=False
    saturday=False
    sunday=False
    for day in worker_Assistence:
        if day.assistDate.weekday() == 0:
            monday=day
        if day.assistDate.weekday() == 1:
            tuesday=day
        if day.assistDate.weekday() == 2:
            wednesday=day
        if day.assistDate.weekday() == 3:
            thursday=day
        if day.assistDate.weekday() == 4:
            friday=day
        if day.assistDate.weekday() == 5:
            saturday=day
        if day.assistDate.weekday() == 6:
            sunday=day
    context = {'worker_Assistence': 'active',
               'monday' : monday, 
               'tuesday' : tuesday, 
               'wednesday' : wednesday, 
               'thursday' : thursday,
               'friday' : friday,
               'saturday' : saturday,
               'sunday' : sunday,
               }
    return render(request, 'Employees/worker_assistence.html', context)
