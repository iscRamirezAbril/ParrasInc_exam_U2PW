from django.shortcuts import render

# Create your views here.
def dashboard_Warehouse(request):
    context = {
        'Almacén' : 'active',
    }
    
    return render(request, 'Warehouse/dashWarehouse.html', context)