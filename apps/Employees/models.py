from email.policy import default
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# |========================================|
# |==========| EMPLOYEES MODELS |==========|
# |========================================|

# |----------| MODEL #1: Employee |----------|
class Employee(models.Model):
    empFirstName=       models.CharField(max_length=50, null = False)
    empLastName=        models.CharField(max_length=50, null = False)
    empBirthDate=       models.DateField(null = True)
    empDateJoined=      models.DateField(auto_now_add=True, null = False)
    empStatus=          models.BooleanField(default=False)
    empEmail=           models.EmailField(max_length=50, null = False)
    empUsername=        models.OneToOneField(User, on_delete=models.CASCADE, null = False)
    
    def __str__(self):
        return self.empFirstName

# |----------| MODEL #2: Department |----------|
class Department(models.Model):
    deptName=           models.CharField(max_length=100)
    
    def __str__(self):
        return self.deptName

# |----------| MODEL #3: job_Position |----------|
class job_Position(models.Model):
    jpName=             models.CharField(max_length=50, null = False)
    jpEmail=            models.EmailField(max_length=50, null = False)
    
    # -----> Foreign Keys <----- #
    # Foreign Key that points to the Department model
    jpDepartment=       models.ForeignKey(Department, on_delete=models.CASCADE, null = False)

    def __str__(self):
        return self.jpName
    
# |----------| MODEL #4: Worker |----------|
class Worker(models.Model):
    workerSalary=       models.DecimalField(max_digits=10, decimal_places=2, null = False)
    workerEntrance=     models.TimeField(null = False)
    workerOut=          models.TimeField(null = False)
    
    # -----> Foreign Keys <----- #
    # Foreign Key that points to the Employee model
    workerEmployee=     models.ForeignKey(Employee, on_delete=models.CASCADE, null = False)
    # Foreign Key that points to the job_Position model
    workerJobPosition=  models.ForeignKey(job_Position, on_delete=models.CASCADE, null = False)
    
    def __str__(self):
        return str(self.workerEmployee)

# |----------| MODEL #5: Assistence |----------|
class Assistence(models.Model):
    assistDate=         models.DateField(auto_now_add=True, null = False)
    
    assistEntrance=     models.TimeField(null = False)
    assistOut=          models.TimeField(null = False)
    
    # -----> Foreign Keys <----- #
    # Foreign Key that points to the Worker model
    assistWorker=        models.ForeignKey(Worker, on_delete=models.CASCADE, null = False)

    def __str__(self):
        return str(self.assistWorker)
        #return self.assistWorker