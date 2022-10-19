from django.contrib import admin

from apps.Production.models import *

# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'areaName']
    
@admin.register(Area_Worker)
class AreaWorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'areaWorkName', 'areaWorkEmployee']