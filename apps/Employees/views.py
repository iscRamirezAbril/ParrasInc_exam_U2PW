from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'index.html')


def Employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            text = 'Welcome back ' + request.user.employee.empFirstName
            messages.success(request, text)
            return redirect('dashboard_admin')

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


def Emp_logout(request):
    logout(request)
    return redirect('emp_login')


def dashboard_admin(request):
    return render(request, 'Employees/dashboard_admin.html')


def dashboard_employee(request):
    return render(request, 'Employees/dashboard_employee.html')