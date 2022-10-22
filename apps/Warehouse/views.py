from django.shortcuts import render

# Create your views here.
def dashboard_Warehouse(request):
    context = {
        'Almacén' : 'active',
    }
    
    return render(request, 'Warehouse/dashWarehouse.html', context)

def warehouse_report(request):
    context = {
        'Almacén' : 'active',
    }
    
    return render(request, 'Warehouse/warehouse_report.html', context)

def warehouse_balance(request):
    context = {
        'Almacén' : 'active',
    }
    
    return render(request, 'Warehouse/warehouse_balance.html', context)