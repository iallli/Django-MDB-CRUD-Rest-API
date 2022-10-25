from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import departmentsSerializer, employeesSerializer

from django.core.files.storage import default_storage

import praw
import datetime

# Create your views here.


@csrf_exempt
def departmentsApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = departmentsSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = departmentsSerializer(data=department_data)

        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(
            department_Id=department_data['department_Id'])
        departments_serializer = departmentsSerializer(
            department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Updated Failed", safe=False)

    elif request.method == 'DELETE':
        department = Departments.objects.get(department_Id=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    return JsonResponse("Delete Failed", safe=False)


@csrf_exempt
def employeesApi(request, id=0):
    # user_agent = "Ali 1.0 by /user/iallli"
    # reddit = praw.Reddit(
    #     client_id='JnvZiIF4j4Du62s36w_rjg',
    #     client_secret='0mPVZ3tcb2vbqCu94TEfw4byJieREw',
    #     user_agent=user_agent
    # )

    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = employeesSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        # print("--------------")
        # print(employee_data)
        # print("--------------")

        # headlines = set()
        # for submission in reddit.subreddit(employee_data.get('key1')).top("all"):

        #     if (submission.selftext == ''):
        #         submission.selftext = 'This user did not comment on this.'

        #     headlines.add(submission.title)
        #     headlines.add(submission.selftext)

        #     print(len(headlines))
        # print(headlines)

        employees_serializer = employeesSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed", safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(
            employee_Id=employee_data['employee_Id'])
        employees_serializer = employeesSerializer(
            employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Updated Failed", safe=False)

    elif request.method == 'DELETE':
        employee = Employees.objects.get(employee_Id=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    return JsonResponse("Delete Failed", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    fileName = default_storage.save(file.name, file)
    return JsonResponse(fileName, safe=False)
