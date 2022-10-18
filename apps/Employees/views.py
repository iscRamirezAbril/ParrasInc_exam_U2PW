from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect


from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout

# |==========| DECORADORES |==========| #
from django.contrib.auth.decorators import *
from apps.Employees.decorators import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

@unauthenticated_user
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
@login_required(login_url='emp_login')
def welcomePage(request):
    return render(request, 'Employees/welcomePage.html')


# Para acceder a esta página, se necesita estar logueado
@login_required(login_url='emp_login')
def dashboard(request):
    return render(request, 'Employees/dashboard.html')

@login_required(login_url='emp_login')
@admin_only
def dashboard_Employees(request):
    return render(request, 'Employees/dashEmployees.html')

def employee_List(request):
    return render(request, 'Employees/employee_List.html')