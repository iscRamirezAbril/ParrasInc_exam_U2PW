from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'deptName']

@admin.register(job_Position)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'jpName', 'jpEmail', 'jpDepartment']
    
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'workerSalary', 'workerEntrance', 'workerOut', 'workerEmployee', 'workerJobPosition']

@admin.register(Assistence)
class WorkerAssistenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'assistWorker', 'assistDate', 'assistEntrance', 'assistOut']