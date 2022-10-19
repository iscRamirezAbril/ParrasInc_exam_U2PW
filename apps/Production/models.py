from django.db import models
from apps.Employees.models import *

# Create your models here.
class Area(models.Model):
    areaName = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.areaName

class Area_Worker(models.Model):
    areaWorkName = models.ForeignKey(Area, on_delete=models.CASCADE, null=False)
    areaWorkEmployee = models.ForeignKey(Worker, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return str(self.areaWorkEmployee)