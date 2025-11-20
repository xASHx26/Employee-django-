from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('<int:pk>/',views.employee_details,name='employee_details')
]