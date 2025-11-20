from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee
def home(request):
    employee=Employee.objects.all()
    context={
        'employee':employee,
    }
    return render(request,'home.html',context)