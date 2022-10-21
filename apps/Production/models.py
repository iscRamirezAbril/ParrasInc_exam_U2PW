from django.db import models
from apps.Employees.models import *

# Create your models here.
class Area(models.Model):
    areaName =                  models.CharField(max_length=50, null=False)
    areaDescription =           models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.areaName

class ProductionLine(models.Model):
    productionLineName =        models.CharField(max_length=50, null=False)
    productionLineDescription = models.CharField(max_length=100, null=False)
    productionLineArea =        models.ForeignKey(Area, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.productionLineName

class LineMember(models.Model):
    lineMemberName =            models.ForeignKey(ProductionLine, on_delete=models.CASCADE, null=False)
    lineMemberWorker =          models.ForeignKey(Worker, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "%s - %s" % (self.lineMemberName, self.lineMemberWorker) # Linea 1 - Materias Primas - David

class Product(models.Model):
    productName =               models.CharField(max_length=50, null=False)
    productDescription =        models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.productName

class ProductOrder(models.Model):
    prodOrdDate =               models.DateField(auto_now=False, auto_now_add=False, null=False)
    prodOrdQuantity =           models.IntegerField(null=False)
    prodOrdActive =             models.BooleanField(default=True)
    prodOrdQuality =            models.BooleanField(default=True)
    prodOrdDone =               models.BooleanField(default=False)
    prodLineMember =            models.ForeignKey(LineMember, on_delete=models.CASCADE, null=False)
    prodOrdProduct =            models.ForeignKey(Product, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "Producto ordenado: %s" % (self.prodOrdProduct.productName)
    
class QualityControl(models.Model):
    qcArea =                    models.ForeignKey(Area, on_delete=models.CASCADE, null=False)
    qcWorker =                  models.ForeignKey(Worker, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "Empleado de calidad %s del area " % (self.qcWorker.workerName, self.qcArea.areaName)

class Part(models.Model):
    partName =                 models.CharField(max_length=100, null=False)
    partWeight =               models.FloatField(null=False)
    partColor =                models.CharField(max_length=50, null=False)

    def __str__(self):
        return "Parte: %s, Peso: %s, Color: %s" % (self.partName, self.partWeight, self.partColor)
    
class PartsQuantity(models.Model):
    pQuantity =              models.IntegerField(null=False)
    pProduct =               models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    pPart =                  models.ForeignKey(Part, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "Cantidad de partes %s de la parte %s del producto %s" % (self.pQuantity, self.pPart ,self.pProduct.productName)
