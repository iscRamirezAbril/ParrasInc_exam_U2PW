from django.contrib import admin

from apps.Parts.models import Category

# Register your models here.
@admin.register(Category)
class QualityControlAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoryName', 'categoryDescription',]