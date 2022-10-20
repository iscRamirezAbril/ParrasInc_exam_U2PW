from django.shortcuts import render
from apps.Production.models import *
# Create your views here.

# |===============| ADMINISTRACIÓN DE PRODUCCIÓN |===============| #
# LISTO #
# Lista de empleados por áreas #
# def worker_Area(request):
#     auto = Area_Worker.objects.filter(areaWorkName = 1)
#     microTec = Area_Worker.objects.filter(areaWorkName = 2)
        
#     return render(request, 'Production/worker_areaList.html', {'auto': auto, 'microTec': microTec})

# Lista de empleados por áreas #
def worker_Area(request):
    areas = Area.objects.all()
    context = {'areasList': areas}
    
    return render(request, 'Production/worker_areaList.html', context)

def dashboard_Production(request):
    return render(request, 'Production/dashProduction.html')