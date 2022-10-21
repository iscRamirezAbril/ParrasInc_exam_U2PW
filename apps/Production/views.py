from django.shortcuts import render
from apps.Production.models import *
# Create your views here.

# |===============| ADMINISTRACIÓN DE PRODUCCIÓN |===============| #
# Lista de empleados por áreas #
def worker_Area(request):
    areas = Area.objects.all() # Obtiene todas las áreas
    workers = LineMember.objects.all() # Obtiene todos los empleados
    lines = ProductionLine.objects.all() # Obtiene todas las líneas de producción
    context = {
            'ETIQUETA,': 'active',
            'areasList': areas,
            'workersList': workers,
            'linesList': lines} # Crea un diccionario con los datos
    
    return render(request, 'Production/worker_areaList.html', context)

# Dashboard de producción #
def dashboard_Production(request):
    return render(request, 'Production/dashProduction.html')