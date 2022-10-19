from django.contrib import admin
from django.urls import path
from apps.Employees.views import *
from apps.Production.views import *

urlpatterns = [
    # |===============| ADMINISTRACIÓN DE PRODUCCIÓN |===============| #
    # LISTO #
    # Lista de empleados por áreas #
    path('worker_area/', worker_Area, name = 'worker_areaList'),
]