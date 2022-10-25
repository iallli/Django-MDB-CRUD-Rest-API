from rest_framework import serializers
from EmployeeApp.models import Departments, Employees


class departmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('department_Id', 'department_Name')


class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('employee_Id', 'employee_Name',
                  'department', 'dateOfJoing', 'photoFileName')
