from django.contrib import admin
from django.urls import path
from apps.Employees.views import *
from apps.Production.views import *

urlpatterns = [
    # |===============| ADMINISTRACIÓN DE PRODUCCIÓN |===============| #
    # TRABAJANDO... #
    # Dashboard de Producción #
    path('dashboard_Production/', dashboard_Production, name='dashboard_Production'),
    # TRABAJANDO... #
    # Lista de empleados por áreas #
    path('worker_area/', worker_Area, name = 'worker_areaList'),
]