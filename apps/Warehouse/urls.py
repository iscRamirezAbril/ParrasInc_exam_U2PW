from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from apps.Warehouse.views import *

urlpatterns = [
    # LISTO #
    # Dashboard para la sección de Almacén #
    path('dashboard_Warehouse/', dashboard_Warehouse, name='dashboard_Warehouse'),
    # PENDIENTE #
    # Reporte de entradas y salidas de materiales #
    path('warehouse_report/', warehouse_report, name='warehouse_report'),
    # PENDIENTE #
    # Balance de piezas y productos #
    path('warehouse_balance/', warehouse_balance, name='warehouse_balance'),
]