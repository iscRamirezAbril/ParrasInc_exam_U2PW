from django.shortcuts import render
from apps.Production.models import *
# Create your views here.
from datetime import *
from django.db.models import Sum

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
    
    areas = Area.objects.all() # Obtiene todas las áreas
    
    context = {
            'Producción': 'active',
            'orders': orders,
            'orders_week': orders_week,
            'orders_day': orders_day,
            'day': day,
            } # Crea un diccionario con los datos
    
    return render(request, 'Production/dashProduction.html', context)

#  #
def dayweek_orders(request):
    
    orders = ProductOrder.objects.all() # Obtiene todas las órdenes de producción
    orders_open = ProductOrder.objects.filter(prodOrdActive=True).distinct() # Obtiene las órdenes abiertas
    orders_close = ProductOrder.objects.filter(prodOrdActive=False).distinct() # Obtiene las órdenes cerradas
    
    orders_close_percentage = (orders_close.count() / orders.count()) * 100 # Calcula el porcentaje de órdenes cerradas
    
    # |===============| PORCENTAJE DE PRODUCTOS POR DÍA |===============| #
    day = date.today() # Obtiene la fecha actual
    # Obtiene las órdenes del día actual (texto) #
    orders_day = ProductOrder.objects.filter(prodOrdDate=date.today()).distinct() # Obtiene las órdenes del día actual
    # Total de ordenes del día actual (numero) #
    orders_today = (orders_day.count())
    
    # Total de productos del día actual #
    today_products = (orders_day.aggregate(Sum('prodOrdQuantity')))
    today_products = today_products.pop('prodOrdQuantity__sum')

    # Porcentaje del total de productos del día de hoy #
    today_products_percentage = (today_products * 100) / 450
    today_products_percentage = round(today_products_percentage, 2)
    
    # |=================================================================| #
    
    orders_week = ProductOrder.objects.filter(prodOrdDate__week=current_week).distinct() # Obtiene las órdenes de la semana actual
    orders_week_num = (orders_week.count()) # Obtiene el número de órdenes de la semana actual
    
    week_products = (orders_week.aggregate(Sum('prodOrdQuantity')))
    week_products = week_products.pop('prodOrdQuantity__sum')
    
    areas = Area.objects.all() # Obtiene todas las áreas
    
    context = {
            'Producción': 'active',
            'orders': orders,
            'orders_week': orders_week,
            'orders_day': orders_day,
            'orders_week_num': orders_week_num,
            'week_products': week_products,
            'day': day,
            'orders_open': orders_open,
            'orders_close': orders_close,
            'orders_close_percentage': orders_close_percentage,
            'areas': areas,
            'orders_today': orders_today,
            'today_products': today_products,
            'today_products_percentage': today_products_percentage
            } # Crea un diccionario con los datos
    
    return render(request, 'Production/dayweek_orders.html', context)

def products_reports(request):
    
    products = Product.objects.all() # Obtiene todos los productos
    orders = ProductOrder.objects.all() # Obtiene todas las órdenes de producción
    areas = Area.objects.all() # Obtiene todas las áreas

    # Obtiene las órdenes del día actual (texto) #
    orders_day = ProductOrder.objects.filter(prodOrdDate=date.today()).distinct() # Obtiene las órdenes del día actual
    # Total de ordenes del día actual (numero) #
    orders_today = (orders_day.count())
    
    # Total de productos del día actual #
    today_products = (orders_day.aggregate(Sum('prodOrdQuantity')))
    today_products = today_products.pop('prodOrdQuantity__sum')
    
    orders_week = ProductOrder.objects.filter(prodOrdDate__week=current_week).distinct() # Obtiene las órdenes de la semana actual


    context = {
            'Producción': 'active',
            'orders': orders,
            'products': products,
            'areas': areas,
            'orders_day': orders_day,
            'orders_week': orders_week,
            } # Crea un diccionario con los datos
    
    return render(request, 'Production/products_reports.html', context)

def qualityControl(request):
        qualityTrue = ProductOrder.objects.filter(prodOrdQuality=True).distinct() # Obtiene las órdenes abiertas
        qualityFalse = ProductOrder.objects.filter(prodOrdQuality=False).distinct() # Obtiene las órdenes cerradas
    
        products = Product.objects.all() # Obtiene todos los productos
        orders = ProductOrder.objects.all() # Obtiene todas las órdenes de producción
    
        context = {
            'Producción': 'active',
            'orders': orders,
            'products': products,
            'qualityTrue': qualityTrue,
            'qualityFalse': qualityFalse,
            } # Crea un diccionario con los datos

        return render(request, 'Production/products_quality.html', context)    

def orders_status(request):
        orders_open = ProductOrder.objects.filter(prodOrdActive=True).distinct() # Obtiene las órdenes abiertas
        orders_close = ProductOrder.objects.filter(prodOrdActive=False).distinct() # Obtiene las órdenes cerradas
    
        products = Product.objects.all() # Obtiene todos los productos
        orders = ProductOrder.objects.all() # Obtiene todas las órdenes de producción
    
        context = {
            'Producción': 'active',
            'orders': orders,
            'products': products,
            'orders_open': orders_open,
            'orders_close': orders_close,
            } # Crea un diccionario con los datos

        return render(request, 'Production/orders_status.html', context)    