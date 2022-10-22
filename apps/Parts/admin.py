from django.contrib import admin
from apps.Parts.models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoryName', 'categoryDescription',]

@admin.register(PartsOrder)
class PartsOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'partsOrdDate', 'partsOrdQuantity', 'partsOrd_ProdOrd', 'partsOrdPart']
    
@admin.register(entryPartOrder)
class entryPartOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'entryPartOrder', 'entryMaterialSheet']