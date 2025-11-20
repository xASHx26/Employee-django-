from django.shortcuts import get_object_or_404, render
from employee.models import Employee
from django.http import Http404, HttpResponse
# Create your views here.
def employee_details(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    context={
        'employee' :employee,
    }
    return render(request,'employee_details.html',context)