from django.db import models
from apps.Production.models import ProductOrder, Part
from apps.Warehouse.models import *

# Create your models here.
class Category(models.Model):
    categoryName =             models.CharField(max_length=50, null=False)
    categoryDescription =      models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return "Categoria: %s" % (self.categoryName)
    
class PartsOrder(models.Model):
    partsOrdDate =            models.DateField(auto_now=False, auto_now_add=False, null=False)
    partsOrdQuantity =        models.IntegerField(null=False)
    partsOrd_ProdOrd =        models.ForeignKey(ProductOrder, on_delete=models.CASCADE, null=False)
    partsOrdPart =            models.ForeignKey(Part, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "Parte ordenada: %s" % (self.partOrderPart.partName)

class entryPartOrder(models.Model):
    entryPartOrder =         models.ForeignKey(PartsOrder, on_delete=models.CASCADE, null=False)
    entryMaterialSheet =     models.CharField(EntryMaterialSheet, max_length=50, null=False)

    def __str__(self):
        return "Parte que entró: %s" % (self.partOrderPart.partName)