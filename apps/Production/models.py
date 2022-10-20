from django.db import models
from apps.Employees.models import *

# Create your models here.
class Area(models.Model):
    areaName = models.CharField(max_length=50, null=False)
    areaDescription = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.areaName

class ProductionLine(models.Model):
    productionLineName = models.CharField(max_length=50, null=False)
    productionLineDescription = models.CharField(max_length=100, null=False)
    productionLineArea = models.ForeignKey(Area, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.productionLineName

class LineMember(models.Model):
    lineMemberName = models.ForeignKey(ProductionLine, on_delete=models.CASCADE, null=False)
    lineMemberWorker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "%s - %s" % (self.lineMemberName, self.lineMemberWorker) # Linea 1 - Materias Primas - David
