from django.contrib import admin
from apps.Warehouse.models import *

# Register your models here.
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['id', 'provName', 'provAddress', 'provContactName', 'provPhone', 'provEmail', 'provRFC', 'provCLABE', 'provAccountNumber', 'provCurrency']

@admin.register(Requsition)
class RequsitionAdmin(admin.ModelAdmin):
    list_display = ['id', 'reqDate', 'reqApprove', 'reqDone', 'reqProvider']

@admin.register(ReqItem)
class ReqItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'reqItemQuantity', 'reqItemPrice', 'reqItemPart', 'reqItemReq']

@admin.register(MaterialSheet)
class ReqItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'matSheetDate', 'matSheetMinQuantity', 'matSheetMaxQuantity', 'matSheetActualQuantity', 'matSheetPart']

@admin.register(EntryMaterialSheet)
class EntryMaterialSheetAdmin(admin.ModelAdmin):
    list_display = ['id', 'entryMSDate', 'entryMSPartsIn', 'entryMSPartsTotal', 'entryMSEmployee', 'entryMSMaterialSheet', 'entryMSReq']
