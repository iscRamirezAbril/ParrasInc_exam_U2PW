from django.shortcuts import render
from apps.Production.models import *
# Create your views here.
from datetime import *

current_week = date.today().isocalendar()[1]

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
    
    orders = ProductOrder.objects.all() # Obtiene todas las órdenes de producción
    orders_week = ProductOrder.objects.filter(prodOrdDate__week=current_week).distinct() # Obtiene las órdenes de la semana actual
    orders_day = ProductOrder.objects.filter(prodOrdDate=date.today()).distinct() # Obtiene las órdenes del día actual
    day = date.today() # Obtiene la fecha actual
    orders_open = ProductOrder.objects.filter(prodOrdActive=True).distinct() # Obtiene las órdenes abiertas
    orders_close = ProductOrder.objects.filter(prodOrdActive=False).distinct() # Obtiene las órdenes cerradas
    
    orders_close_percentage = (orders_close.count() / orders.count()) * 100 # Calcula el porcentaje de órdenes cerradas
    
    areas = Area.objects.all() # Obtiene todas las áreas
    
    context = {
            'ETIQUETA,': 'active',
            'orders': orders,
            'orders_week': orders_week,
            'orders_day': orders_day,
            'day': day,
            'orders_open': orders_open,
            'orders_close': orders_close,
            'orders_close_percentage': orders_close_percentage,
            'areas': areas,
            } # Crea un diccionario con los datos
    
    return render(request, 'Production/dashProduction.html', context)