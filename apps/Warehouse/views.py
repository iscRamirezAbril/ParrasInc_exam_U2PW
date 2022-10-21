from django.shortcuts import render

# Create your views here.
def dashboard_Warehouse(request):
    return render(request, 'Warehouse/dashWarehouse.html')