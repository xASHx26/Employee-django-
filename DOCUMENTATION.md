# Employee Management System - Complete Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Installation & Setup](#installation--setup)
4. [How the Application Works](#how-the-application-works)
5. [Step-by-Step Operation Flow](#step-by-step-operation-flow)
6. [Database Models](#database-models)
7. [URL Routing](#url-routing)
8. [Views](#views)
9. [Templates](#templates)
10. [Static Files](#static-files)
11. [How to Use](#how-to-use)

---

## Project Overview

This is a **Django-based Employee Management System** that allows you to:
- View a list of all employees
- Click on an employee to view their detailed information
- Navigate between the employee list and individual employee details
- Display employee information including photos, contact details, designation, and timestamps

**Technology Stack:**
- Backend: Django 5.2.8
- Database: SQLite3
- Frontend: Bootstrap 5.3.8
- Image Handling: Pillow (Python Imaging Library)

---

## Project Structure

```
employee django udemy/
├── db.sqlite3                 # SQLite database file
├── manage.py                  # Django management script
├── DOCUMENTATION.md           # This file
├── env/                       # Python virtual environment
│   ├── Lib/site-packages/    # Installed packages (Django, Pillow, etc.)
│   └── Scripts/              # Virtual environment executables
├── mysite/                    # Main Django project folder
│   ├── __init__.py
│   ├── settings.py            # Django configuration settings
│   ├── urls.py                # Main URL routing configuration
│   ├── views.py               # Main project views
│   ├── wsgi.py                # WSGI application
│   ├── asgi.py                # ASGI application
│   ├── __pycache__/
│   └── static/                # Static files (CSS, images)
│       ├── css/
│       │   └── style.css      # Custom CSS styles
│       └── images/            # Static images
├── employee/                  # Django app for employee management
│   ├── __init__.py
│   ├── models.py              # Employee database model
│   ├── views.py               # Employee views
│   ├── urls.py                # Employee URL routing
│   ├── admin.py               # Django admin configuration
│   ├── apps.py                # App configuration
│   ├── tests.py               # Unit tests
│   ├── migrations/            # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py   # Initial migration
│   ├── __pycache__/
│   └── __init__.py
├── templates/                 # HTML templates folder
│   ├── home.html              # Employee list page
│   └── employee_details.html  # Employee detail page
└── media/                     # User-uploaded media (employee photos)
    └── images/                # Employee image uploads
```

---

## Installation & Setup

### Step 1: Create Virtual Environment
```bash
python -m venv env
```

### Step 2: Activate Virtual Environment
**Windows:**
```bash
env\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source env/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install django
pip install pillow  # For image handling
```

### Step 4: Apply Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Server runs on: `http://127.0.0.1:8000/`

---

## How the Application Works

### High-Level Overview

```
User Browser
    ↓
    ├─→ Request to / (Home Page)
    │   └─→ Views.home() loads all employees
    │       └─→ Renders home.html with employee list
    │           └─→ User sees employee table with links
    │
    └─→ Click on Employee Name
        └─→ Request to /employee/{id}/ (Detail Page)
            └─→ Views.employee_details() loads specific employee
                └─→ Renders employee_details.html
                    └─→ User sees full employee information
                        └─→ Click "Back to Home" button
                            └─→ Back to home page
```

---

## Step-by-Step Operation Flow

### **STEP 1: Django Server Starts**

When you run `python manage.py runserver`:
1. Django loads all settings from `mysite/settings.py`
2. Django registers all installed apps including 'employee'
3. Django loads all URL patterns from `mysite/urls.py`
4. Django establishes database connection (SQLite3)
5. Server listens on `http://127.0.0.1:8000`

---

### **STEP 2: User Visits Homepage (http://127.0.0.1:8000/)**

**What happens:**

1. **Browser sends HTTP GET request**
   ```
   GET / HTTP/1.1
   Host: 127.0.0.1:8000
   ```

2. **Django URL Router matches the URL**
   - In `mysite/urls.py`, Django checks: `path('',views.home,name='home')`
   - Matches empty path `''` to the homepage
   - Calls `views.home()` function

3. **View Function Executes (`mysite/views.py`)**
   ```python
   def home(request):
       employee=Employee.objects.all()  # Query all employees from DB
       context={
           'employee':employee,
       }
       return render(request,'home.html',context)
   ```
   - Queries database for ALL Employee records
   - Packages employee data into a dictionary called `context`
   - Renders `home.html` template with the context

4. **Template Processes Data (`templates/home.html`)**
   ```html
   {% for emp in employee %}
       <tr>
           <th scope="row">{{forloop.counter}}</th>
           <td><a href="{% url 'employee:employee_details' emp.id %}">
               {{emp.first_name}} {{emp.last_name}}
           </a></td>
           <td>{{emp.designation}}</td>
           <td>{{emp.phone_number}}</td>
       </tr>
   {% endfor %}
   ```
   - Django template engine loops through each employee
   - Creates a table row for each employee
   - `forloop.counter` auto-increments the row number
   - `{% url %}` tag generates the URL to employee details page

5. **HTML is Rendered**
   - Bootstrap CSS is loaded from CDN
   - Table with all employees is displayed
   - Each employee name is a clickable link

6. **Browser Displays Page**
   - User sees employee list table
   - Table contains: ID, Full Name, Designation, Phone Number

---

### **STEP 3: User Clicks on Employee Name**

Example: Click on "Mark Otto"

**What happens:**

1. **Browser sends HTTP GET request**
   ```
   GET /employee/1/ HTTP/1.1
   Host: 127.0.0.1:8000
   ```
   (Assuming Mark Otto has ID = 1)

2. **Django URL Router matches the URL**
   - In `mysite/urls.py`: `path('employee/',include('employee.urls',namespace='employee'))`
   - Routes to `employee/urls.py`
   - In `employee/urls.py`: `path('<int:pk>/',views.employee_details,name='employee_details')`
   - `<int:pk>` captures the employee ID (1) as parameter `pk`
   - Calls `employee_details()` view with `pk=1`

3. **View Function Executes (`employee/views.py`)**
   ```python
   def employee_details(request,pk):
       employee=get_object_or_404(Employee,pk=pk)
       context={
           'employee' :employee,
       }
       return render(request,'employee_details.html',context)
   ```
   - `get_object_or_404()` retrieves ONE employee where `id=pk` (1)
   - If employee doesn't exist, shows 404 error page
   - Packages employee data into context
   - Renders `employee_details.html`

4. **Database Query**
   ```sql
   SELECT * FROM employee_employee WHERE id = 1;
   ```
   - SQLite finds the employee with ID 1
   - Returns all fields: first_name, last_name, photo, designation, email_adress, phone_number, created_at, updated_at

5. **Template Processes Data (`templates/employee_details.html`)**
   ```html
   <img class="card-img-top" src="{{ employee.photo.url }}" alt="Card image cap">
   <div class="card-body">
       <p><strong>Name:</strong> {{ employee.first_name }} {{ employee.last_name }}</p>
       <p><strong>Email:</strong> {{ employee.email_adress }}</p>
       <p><strong>Designation:</strong> {{ employee.designation }}</p>
       <p><strong>Phone:</strong> {{ employee.phone_number }}</p>
       <p><strong>Created:</strong> {{ employee.created_at }}</p>
       <p><strong>Updated:</strong> {{ employee.updated_at }}</p>
   </div>
   ```
   - `{{ employee.photo.url }}` displays the employee's photo
   - `{{ employee.first_name }}` displays first name
   - Other fields display their values
   - Bootstrap card styling makes it look nice

6. **HTML is Rendered**
   - Employee card with photo is displayed
   - All details are shown clearly
   - "Back to home" button appears at bottom

7. **Browser Displays Page**
   - User sees detailed employee information
   - Employee photo is displayed (if uploaded)
   - All contact and designation information visible

---

### **STEP 4: User Clicks "Back to Home" Button**

**What happens:**

1. **HTML Link in Template**
   ```html
   <a href="{% url 'home' %}" class="btn btn-primary">Back to home</a>
   ```
   - `{% url 'home' %}` is Django template tag
   - Translates to: `href="/"`
   - Browser sends GET request to home page

2. **Process Repeats**
   - Same as STEP 2
   - User returns to employee list

---

## Database Models

### Employee Model (`employee/models.py`)

```python
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_adress = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Field Explanations:**

| Field | Type | Purpose |
|-------|------|---------|
| `first_name` | CharField | Employee's first name (max 100 chars) |
| `last_name` | CharField | Employee's last name (max 100 chars) |
| `photo` | ImageField | Employee's profile photo (stored in media/images/) |
| `designation` | CharField | Job title (max 100 chars) |
| `email_adress` | EmailField | Email (unique - no duplicates allowed) |
| `phone_number` | CharField | Phone number (optional - blank=True) |
| `created_at` | DateTimeField | When record was created (auto-filled) |
| `updated_at` | DateTimeField | When record was last modified (auto-filled) |

**Database Table Name:** `employee_employee`

---

## URL Routing

### Main URLs (`mysite/urls.py`)

```python
urlpatterns = [
    path('admin/', admin.site.urls),                           # Django admin
    path('',views.home,name='home'),                           # Home page
    path('employee/',include('employee.urls',namespace='employee'))  # Employee URLs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Breakdown:**

| URL Pattern | View | Name | Purpose |
|------------|------|------|---------|
| `/admin/` | Django Admin | `admin` | Admin interface |
| `/` | `views.home` | `home` | Employee list page |
| `/employee/<id>/` | `employee_details` | `employee:employee_details` | Employee detail page |

### Employee URLs (`employee/urls.py`)

```python
app_name = 'employee'  # Namespace for this app

urlpatterns = [
    path('<int:pk>/',views.employee_details,name='employee_details')
]
```

**Explanation:**
- `<int:pk>` captures integer ID from URL
- Example: `/employee/1/` → `pk=1`
- `app_name = 'employee'` creates namespace
- Full URL name: `employee:employee_details`

---

## Views

### Home View (`mysite/views.py`)

```python
from django.shortcuts import render
from employee.models import Employee

def home(request):
    employee = Employee.objects.all()  # Get all employees
    context = {
        'employee': employee,
    }
    return render(request, 'home.html', context)
```

**Process:**
1. Query ALL employees from database
2. Pass to template as `employee` variable
3. Template loops through and displays in table

---

### Employee Details View (`employee/views.py`)

```python
from django.shortcuts import get_object_or_404, render
from employee.models import Employee

def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)  # Get one employee or 404
    context = {
        'employee': employee,
    }
    return render(request, 'employee_details.html', context)
```

**Process:**
1. Get employee ID from URL parameter (`pk`)
2. Query database for that specific employee
3. If not found, show 404 error
4. Pass to template as `employee` variable
5. Template displays all details

---

## Templates

### Home Template (`templates/home.html`)

**Key Parts:**

```html
{% load static %}
```
- Loads Django static files module for CSS/JS/images

```html
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```
- Loads custom CSS

```html
<table class="table">
    {% for emp in employee %}
    <tr>
        <th scope="row">{{forloop.counter}}</th>
        <td><a href="{% url 'employee:employee_details' emp.id %}">
            {{emp.first_name}} {{emp.last_name}}
        </a></td>
        <td>{{emp.designation}}</td>
        <td>{{emp.phone_number}}</td>
    </tr>
    {% endfor %}
</table>
```

**Explanation:**
- `{% for emp in employee %}` loops through all employees
- `{{forloop.counter}}` auto-increments (1, 2, 3...)
- `{% url 'employee:employee_details' emp.id %}` generates `/employee/{id}/`
- Each employee name is a clickable link

---

### Employee Details Template (`templates/employee_details.html`)

```html
<img src="{{ employee.photo.url }}" alt="Card image cap">
<div class="card-body">
    <p><strong>Name:</strong> {{ employee.first_name }} {{ employee.last_name }}</p>
    <p><strong>Email:</strong> {{ employee.email_adress }}</p>
    <p><strong>Designation:</strong> {{ employee.designation }}</p>
    <p><strong>Phone:</strong> {{ employee.phone_number }}</p>
    <p><strong>Created:</strong> {{ employee.created_at }}</p>
    <p><strong>Updated:</strong> {{ employee.updated_at }}</p>
</div>
<a href="{% url 'home' %}" class="btn btn-primary">Back to home</a>
```

**Explanation:**
- `{{ employee.photo.url }}` displays employee photo
- All employee details displayed in Bootstrap card
- `{% url 'home' %}` generates link back to home page

---

## Static Files

### Directory Structure
```
mysite/static/
├── css/
│   └── style.css          # Custom CSS styles
└── images/                # Static images
```

### Settings in `mysite/settings.py`
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = ['mysite/static']
STATIC_ROOT = WindowsPath('E:/project/employee django udemy/static')
```

**Explanation:**
- `STATIC_URL` - URL prefix for static files (/static/)
- `STATICFILES_DIRS` - Where to find static files during development
- `STATIC_ROOT` - Where Django collects static files for production

---

## Settings Configuration

### Key Settings in `mysite/settings.py`

```python
# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employee',  # Our employee app
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],  # Where templates are located
        'APP_DIRS': True,
    }
]

# Media Files (User Uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## How to Use

### 1. Add a New Employee

**Using Django Admin:**
1. Go to `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials
3. Click on "Employees"
4. Click "Add Employee"
5. Fill in all fields (photo is required)
6. Save

**Using Django Shell:**
```bash
python manage.py shell
```
```python
from employee.models import Employee

Employee.objects.create(
    first_name="John",
    last_name="Doe",
    designation="Developer",
    email_adress="john@example.com",
    phone_number="1234567890"
)
```

### 2. View All Employees
- Go to `http://127.0.0.1:8000/`
- See table with all employees

### 3. View Employee Details
- Click on employee name from list
- See detailed card with photo and all info

### 4. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
- Username: (enter your choice)
- Email: (enter your email)
- Password: (enter secure password)

### 5. Make Migrations (After Model Changes)
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: No module named 'employee'` | App not installed | Add `'employee'` to INSTALLED_APPS in settings.py |
| `NoReverseMatch` | URL name not found | Check `app_name` in employee/urls.py |
| `Reverse for 'employee_details' not found` | Missing namespace | Use `'employee:employee_details'` instead of `'employee_details'` |
| Image not displaying | Photo field is empty | Upload photo in admin or via model creation |
| `405 Method Not Allowed` | Wrong HTTP method | Use GET requests, not POST |

---

## Database Diagram

```
┌─────────────────────────────────────┐
│      employee_employee (Table)      │
├─────────────────────────────────────┤
│ id (Primary Key)                    │
│ first_name (CharField)              │
│ last_name (CharField)               │
│ photo (ImageField)                  │
│ designation (CharField)             │
│ email_adress (EmailField, Unique)   │
│ phone_number (CharField, Nullable)  │
│ created_at (DateTimeField)          │
│ updated_at (DateTimeField)          │
└─────────────────────────────────────┘
```

---

## Request/Response Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERACTION                         │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────┐
        │  Browser sends HTTP Request       │
        │  GET / or GET /employee/1/        │
        └──────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────┐
        │   Django URL Router               │
        │   matches URL pattern             │
        └──────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────┐
        │   View Function Executes          │
        │   home() or employee_details()    │
        └──────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────┐
        │   Database Query                  │
        │   via Employee.objects.all()      │
        │   or get_object_or_404()          │
        └──────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────┐
        │   Template Engine Renders         │
        │   home.html or employee_details   │
        │   with context data               │
        └──────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────┐
        │   HTML Sent to Browser            │
        │   with CSS & Images               │
        └──────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────┐
        │   Browser Displays Page           │
        │   User sees content               │
        └──────────────────────────────────┘
```

---

## Summary

This Employee Management System works by:

1. **Starting the server** - Django initializes and listens for requests
2. **User visits home page** - Views fetch all employees from database
3. **Template renders list** - HTML table displays each employee as clickable link
4. **User clicks employee** - URL captures employee ID and passes to detail view
5. **Detail view fetches employee** - Specific employee record retrieved from database
6. **Template renders details** - Employee information displayed in card format
7. **User returns home** - Click "Back to Home" button returns to employee list

All data flows from Database → Views → Templates → Browser → User Display

---

**Created:** November 19, 2025  
**Django Version:** 5.2.8  
**Python Version:** 3.11.0
