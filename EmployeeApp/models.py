from django.db import models

# Create your models here.


class Departments(models.Model):
    department_Id = models.AutoField(primary_key=True)
    department_Name = models.CharField(max_length=255)


class Employees(models.Model):
    employee_Id = models.AutoField(primary_key=True)
    employee_Name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    dateOfJoing = models.DateField()
    photoFileName = models.CharField(max_length=255)
