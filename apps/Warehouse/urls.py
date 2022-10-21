from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from apps.Warehouse.views import *

urlpatterns = [
    path('dashboard_Warehouse/', dashboard_Warehouse, name='dashboard_Warehouse'),
]