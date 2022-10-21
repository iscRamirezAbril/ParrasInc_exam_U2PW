from django.contrib import admin
from django.urls import path
from apps.Employees.views import *
from apps.Production.views import *

urlpatterns = [
    # |===============| ADMINISTRACIÓN DE PRODUCCIÓN |===============| #
    # LISTO #
    # Dashboard de Producción #
    path('dashboard_Production/', dashboard_Production, name='dashboard_Production'),
    # LISTO #
    # Lista de empleados por áreas #
    path('worker_area/', worker_Area, name = 'worker_areaList'),
    # LISTO #
    # Reportes de ordenes por días y semanas #
    path('dayweek_orders/', dayweek_orders, name = 'dayweek_orders'),
    # LISTO #
    # Reportes de productos #
    path('products_reports/', products_reports, name = 'products_reports'),
    # LISTO #
    # Reportes de productos aprobados y no aprobados por calidad #
    path('products_quality', qualityControl, name = 'products_quality'),
    # LISTO #
    # Reportes de ordenes con estatus abierto y cerrado #
    path('orders_status', orders_status, name = 'orders_status'),
]