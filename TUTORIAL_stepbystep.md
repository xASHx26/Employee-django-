# Django Employee Management System - Complete Tutorial

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Project Setup](#project-setup)
4. [Creating the Employee App](#creating-the-employee-app)
5. [Database Configuration](#database-configuration)
6. [Creating Models](#creating-models)
7. [Admin Configuration](#admin-configuration)
8. [URL Configuration](#url-configuration)
9. [Views Setup](#views-setup)
10. [Templates Creation](#templates-creation)
11. [Running the Server](#running-the-server)

---

## Prerequisites

### Requirements
- Python 3.8 or higher
- pip (Python package manager)
- A code editor (VS Code, PyCharm, etc.)
- Basic command line knowledge

### Check Python Installation
```bash
python --version
pip --version
```

---

## Installation

### Step 1: Create a Project Directory
```bash
mkdir employee-django
cd employee-django
```

### Step 2: Create a Virtual Environment
```bash
# Windows
python -m venv env

# macOS/Linux
python3 -m venv env
```

### Step 3: Activate Virtual Environment
```bash
# Windows (PowerShell)
.\env\Scripts\Activate.ps1

# Windows (Command Prompt)
env\Scripts\activate

# macOS/Linux
source env/bin/activate
```

### Step 4: Install Django and Dependencies
```bash
pip install django
pip install django-phonenumber-field
pip install phonenumbers
pip install pillow
```

---

## Project Setup

### Step 5: Create Django Project
```bash
django-admin startproject mysite
cd mysite
```

### Step 6: Project Structure
After creation, your structure should look like:
```
employee-django/
├── env/                    # Virtual environment
├── mysite/                 # Project directory
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL configuration
│   ├── asgi.py
│   ├── wsgi.py
├── manage.py              # Django management script
├── db.sqlite3             # Database (created later)
```

---

## Creating the Employee App

### Step 7: Create App
```bash
python manage.py startapp employees
```

### Step 8: Register App in Settings
Open `mysite/settings.py` and add 'employees' to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employees',  # Add this line
]
```

---

## Database Configuration

### Step 9: Configure Media Files (for image uploads)
In `mysite/settings.py`, add at the end:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Step 10: Configure Templates
In `mysite/settings.py`, update TEMPLATES:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

## Creating Models

### Step 11: Define Employee Model
Open `employees/models.py`:

```python
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = PhoneNumberField(unique=True)
    photo = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
```

---

## Admin Configuration

### Step 12: Register Model in Admin
Open `employees/admin.py`:

```python
from django.contrib import admin
from .models import Employee

admin.site.register(Employee)
```

---

## URL Configuration

### Step 13: Create Employees URLs
Create `employees/urls.py`:

```python
from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('employee_details/<int:pk>/', views.employee_details, name='employee_details'),
]
```

### Step 14: Update Main URLs
Open `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('employee/', include('employees.urls', namespace='employee')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## Views Setup

### Step 15: Create Views
Open `mysite/views.py`:

```python
from django.shortcuts import render, get_object_or_404
from employees.models import Employee

def home(request):
    employee = Employee.objects.all()
    context = {
        'employee': employee,
    }
    return render(request, 'home.html', context)
```

### Step 16: Create Employee Details View
Open `employees/views.py`:

```python
from django.shortcuts import get_object_or_404, render
from employees.models import Employee

def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee': employee,
    }
    return render(request, 'employee_details.html', context)
```

---

## Templates Creation

### Step 17: Create Templates Directory
```bash
mkdir templates
```

### Step 18: Create home.html
Create `templates/home.html`:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Management System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
            padding: 20px 0;
        }
        .container {
            margin-top: 30px;
        }
        .page-header h1 {
            color: #333;
            font-weight: bold;
            border-bottom: 3px solid #007bff;
            padding-bottom: 15px;
            margin-bottom: 30px;
        }
        .table {
            background-color: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }
        .table thead {
            background-color: #007bff;
            color: white;
        }
        .table tbody tr:hover {
            background-color: #f8f9fa;
        }
        .table a {
            color: #007bff;
            text-decoration: none;
        }
        .table a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="page-header">
            <h1>👥 Employee Management System</h1>
        </div>
        
        {% if employee %}
            <div class="table-responsive">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>No</th>
                            <th>Full Name</th>
                            <th>Email</th>
                            <th>Phone</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for emp in employee %}
                        <tr>
                            <td>{{ forloop.counter }}</td>
                            <td><a href="{% url 'employee:employee_details' emp.pk %}">{{ emp.first_name }} {{ emp.last_name }}</a></td>
                            <td>{{ emp.email }}</td>
                            <td>{{ emp.phone }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        {% else %}
            <div class="alert alert-info">
                📭 No employees found.
            </div>
        {% endif %}
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### Step 19: Create employee_details.html
Create `templates/employee_details.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Details</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding: 20px 0;
        }
        .card {
            border: none;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            border-radius: 15px;
        }
        .card-img-top {
            height: 300px;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    {% if employee.photo %}
                        <img src="{{ employee.photo.url }}" class="card-img-top" alt="Employee">
                    {% endif %}
                    
                    <div class="card-body">
                        <h2 class="card-title">{{ employee.first_name }} {{ employee.last_name }}</h2>
                        <p><strong>Email:</strong> {{ employee.email }}</p>
                        <p><strong>Phone:</strong> {{ employee.phone }}</p>
                        <a href="{% url 'home' %}" class="btn btn-primary">← Back to List</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

---

## Database Migrations

### Step 20: Create Migrations
```bash
python manage.py makemigrations
```

### Step 21: Apply Migrations
```bash
python manage.py migrate
```

---

## Running the Server

### Step 22: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 23: Run Development Server
```bash
python manage.py runserver
```

### Step 24: Access Your Application

1. **Home Page:** http://127.0.0.1:8000/
2. **Admin Panel:** http://127.0.0.1:8000/admin/
3. **Employee Details:** http://127.0.0.1:8000/employee/employee_details/1/

---

## Adding Employees

1. Go to http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Click "Add Employee"
4. Fill in the details:
   - First Name
   - Last Name
   - Email
   - Phone (in international format, e.g., +1234567890)
   - Photo (upload an image)
5. Click "Save"

---

## Complete Project Structure

```
employee-django/
├── env/
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── views.py
├── employees/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── home.html
│   └── employee_details.html
├── media/
│   └── images/
├── manage.py
└── db.sqlite3
```

---

## Troubleshooting

### Issue: "No module named 'django'"
**Solution:** Make sure your virtual environment is activated
```bash
# Windows
.\env\Scripts\Activate.ps1

# macOS/Linux
source env/bin/activate
```

### Issue: "ModuleNotFoundError: No module named 'employees'"
**Solution:** Make sure 'employees' is added to INSTALLED_APPS in settings.py

### Issue: "TemplateDoesNotExist"
**Solution:** Verify the templates directory path in settings.py matches your folder structure

### Issue: Images not showing
**Solution:** Make sure MEDIA_URL and MEDIA_ROOT are configured in settings.py

---

## Next Steps

1. Add more features (edit, delete employees)
2. Add authentication
3. Add search and filtering
4. Deploy to a production server
5. Add CSS styling
6. Add form validation

---

## Useful Commands

```bash
# Create new app
python manage.py startapp app_name

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Shell (interactive Python shell)
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic
```

---

## Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django URLs](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

---

**Happy Django Development! 🚀**
