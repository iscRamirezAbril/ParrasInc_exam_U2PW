from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='emp_login')
def dashboard_Warehouse(request):
    context = {
        'Almacén' : 'active',
    }
    
    return render(request, 'Warehouse/dashWarehouse.html', context)

@login_required(login_url='emp_login')
def warehouse_report(request):
    context = {
        'Almacén' : 'active',
    }
    
    return render(request, 'Warehouse/warehouse_report.html', context)

@login_required(login_url='emp_login')
def warehouse_balance(request):
    context = {
        'Almacén' : 'active',
    }
    
    return render(request, 'Warehouse/warehouse_balance.html', context)