from django.db import models
from apps.Employees.models import Employee
from apps.Parts.models import Part

# Create your models here.
class Provider(models.Model):
    provName =                  models.CharField(max_length=100, null=False)
    provAddress =               models.CharField(max_length=100, null=False)
    provContactName =           models.CharField(max_length=50, null=False)
    provPhone =                 models.CharField(max_length=50, null=False)
    provEmail =                 models.EmailField(max_length=50, null=False)
    provRFC =                   models.CharField(max_length=50, null=False)
    provCLABE =                 models.CharField(max_length=50, null=False)
    provAccountNumber =         models.CharField(max_length=50, null=False)
    provCurrency =              models.CharField(max_length=50, null=False)

    def __str__(self):
        return "Proveedor: %s" % (self.provName)

class Requsition(models.Model):
    reqDate =              models.DateField(auto_now=False, auto_now_add=False, null=False)
    reqApprove =           models.BooleanField(default=False)
    reqDone =              models.BooleanField(default=False)
    reqProvider =          models.ForeignKey(Provider, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return "Requisición: %s" % (self.reqDate)

class ReqItem(models.Model):
    reqItemQuantity =          models.IntegerField(null=False)
    reqItemPrice =             models.DecimalField(max_digits=10, decimal_places=2, null=False)
    reqItemPart =              models.ForeignKey(Part, on_delete=models.CASCADE, null=False)
    reqItemReq =               models.ForeignKey(Requsition, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "Requisición: %s" % (self.reqItemReq.reqDate)

class MaterialSheet(models.Model):
    matSheetDate =              models.DateField(auto_now=False, auto_now_add=False, null=False)
    matSheetMinQuantity =       models.IntegerField(null=False)
    matSheetMaxQuantity =       models.IntegerField(null=False)
    matSheetActualQuantity =    models.IntegerField(null=False)
    matSheetPart =              models.ForeignKey(Part, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "Hoja de salida de material: %s" % (self.exitMaterialSheet)

class EntryMaterialSheet(models.Model):
    entryMSDate =          models.DateField(auto_now=False, auto_now_add=False, null=False)
    entryMSPartsIn =       models.IntegerField(null=False)
    entryMSPartsTotal =    models.IntegerField(null=False)
    entryMSEmployee =      models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    entryMSMaterialSheet = models.ForeignKey(MaterialSheet, on_delete=models.CASCADE, null=False)
    entryMSReq =           models.ForeignKey(Requsition, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return "Hoja de entrada de material: %s" % (self.entryMaterialSheet)
