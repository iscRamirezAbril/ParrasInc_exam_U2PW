from django.contrib import admin

from apps.Production.models import *

# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'areaName']

@admin.register(ProductionLine)
class ProductionLineAdmin(admin.ModelAdmin):
    list_display = ['id', 'productionLineName', 'productionLineDescription', 'productionLineArea',]

@admin.register(LineMember)
class ProductionLineAdmin(admin.ModelAdmin):
    list_display = ['id', 'lineMemberName', 'lineMemberWorker',]