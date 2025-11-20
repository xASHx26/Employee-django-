# Employee Management System - Complete Tutorial

## 📚 Table of Contents
1. [Getting Started](#getting-started)
2. [Tutorial 1: Setup & Installation](#tutorial-1-setup--installation)
3. [Tutorial 2: Understanding the Project Structure](#tutorial-2-understanding-the-project-structure)
4. [Tutorial 3: Working with the Database](#tutorial-3-working-with-the-database)
5. [Tutorial 4: Creating Your First Employee](#tutorial-4-creating-your-first-employee)
6. [Tutorial 5: Viewing the Employee List](#tutorial-5-viewing-the-employee-list)
7. [Tutorial 6: Viewing Employee Details](#tutorial-6-viewing-employee-details)
8. [Tutorial 7: Managing Employees via Admin Panel](#tutorial-7-managing-employees-via-admin-panel)
9. [Tutorial 8: Customizing the Application](#tutorial-8-customizing-the-application)
10. [Troubleshooting Guide](#troubleshooting-guide)

---

## Getting Started

**Prerequisites:**
- Python 3.11+ installed
- Git installed
- Text editor (VS Code recommended)
- Basic command line knowledge

**What You'll Learn:**
- How to set up Django project from scratch
- How models, views, and templates work together
- How to create and manage employee records
- How to customize the application

---

## Tutorial 1: Setup & Installation

### Step 1.1: Open Command Line

**Windows:**
- Press `Win + R`
- Type `powershell`
- Press Enter

**Mac/Linux:**
- Press `Ctrl + Alt + T`

### Step 1.2: Navigate to Project Directory

```bash
cd e:\project\employee\ django\ udemy
```

### Step 1.3: Create Virtual Environment

```bash
python -m venv env
```

**What this does:**
- Creates a `env` folder
- Isolates your project's Python packages
- Prevents conflicts with system Python

### Step 1.4: Activate Virtual Environment

**Windows (PowerShell):**
```bash
env\Scripts\Activate.ps1
```

**If you get an error about execution policy:**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then run the activation command again.

**Windows (Command Prompt):**
```bash
env\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source env/bin/activate
```

**How to know it worked:**
```
(env) PS E:\project\employee django udemy>
```
Notice `(env)` prefix - this means virtual environment is active!

### Step 1.5: Install Django

```bash
pip install django
```

**What this does:**
- Downloads and installs Django framework
- Allows you to use Django commands

### Step 1.6: Install Pillow (Image Library)

```bash
pip install pillow
```

**What this does:**
- Installs image processing library
- Allows handling employee photos

### Step 1.7: Apply Migrations

```bash
python manage.py migrate
```

**What this does:**
- Creates database tables for Django admin, users, sessions
- Sets up SQLite database
- Creates `db.sqlite3` file

### Step 1.8: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

**You'll be prompted for:**
```
Username: admin
Email: admin@example.com
Password: ••••••••
Password (again): ••••••••
```

**Tips:**
- Username: use something simple like "admin"
- Password: use something secure but memorable
- Email: doesn't need to be real

### Step 1.9: Start Development Server

```bash
python manage.py runserver
```

**You should see:**
```
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
November 20, 2025 - 10:00:00
Django version 5.2.8, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 1.10: Open Application in Browser

1. Open web browser
2. Go to: `http://127.0.0.1:8000/`
3. You should see the employee list page (empty for now)

**Congratulations!** ✅ Your application is running!

---

## Tutorial 2: Understanding the Project Structure

Let's explore what each folder does:

### Folder Breakdown

**`env/` - Virtual Environment**
```
Contains all installed packages (Django, Pillow, etc.)
This is like a "Python toolbox" for your project
```

**`mysite/` - Main Django Project**
```
settings.py  ← Configuration file (database, apps, templates, etc.)
urls.py      ← Main URL routing (which URL goes to which view)
views.py     ← Main view functions
```

**`employee/` - Employee App**
```
models.py    ← Database structure (Employee table)
views.py     ← View functions for employee pages
urls.py      ← URL routing for employee pages
admin.py     ← Admin panel configuration
```

**`templates/` - HTML Files**
```
home.html              ← Employee list page
employee_details.html  ← Employee detail page
```

**`media/` - User Uploads**
```
This folder stores employee photos when uploaded
```

**`db.sqlite3` - Database**
```
This is where all employee data is stored
It's a SQLite database file
```

### File Purpose Chart

| File | Purpose | Edit? |
|------|---------|-------|
| `settings.py` | Configuration | Sometimes |
| `urls.py` | URL routing | Rarely |
| `models.py` | Database structure | When adding features |
| `views.py` | Business logic | Often |
| `home.html` | Employee list design | Often |
| `employee_details.html` | Detail page design | Often |
| `admin.py` | Admin panel setup | Rarely |

---

## Tutorial 3: Working with the Database

### What is a Database?

A database is like a spreadsheet that stores all your data:

```
Employee Table
┌────┬────────┬─────────┬─────────────────┬──────────────┐
│ ID │ First  │ Last    │ Designation     │ Email        │
├────┼────────┼─────────┼─────────────────┼──────────────┤
│ 1  │ John   │ Doe     │ Developer       │ john@email   │
│ 2  │ Jane   │ Smith   │ Manager         │ jane@email   │
│ 3  │ Mark   │ Johnson │ Designer        │ mark@email   │
└────┴────────┴─────────┴─────────────────┴──────────────┘
```

### Django Models = Database Tables

In `employee/models.py`:
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

**Translation:**
```
Each line = one column in the database

CharField        = Text (up to max_length characters)
ImageField       = Image file
EmailField       = Email address (validated format)
DateTimeField    = Date and time
unique=True      = No duplicate values allowed
blank=True       = Field is optional
auto_now_add=True = Automatically set when created
auto_now=True    = Automatically update when modified
```

### Making Migrations

When you change a model, you need to tell Django:

```bash
python manage.py makemigrations
```

**What this does:**
- Detects changes in `models.py`
- Creates migration file in `migrations/` folder
- This file describes what changed

Then apply the changes:

```bash
python manage.py migrate
```

**What this does:**
- Executes migration files
- Updates database structure
- Adds/removes/modifies columns

---

## Tutorial 4: Creating Your First Employee

### Method 1: Using Admin Panel (Easiest)

**Step 1:** Go to admin panel
```
http://127.0.0.1:8000/admin/
```

**Step 2:** Login with superuser credentials
```
Username: admin
Password: (your password)
```

**Step 3:** Click "Employees"

**Step 4:** Click "Add Employee" button

**Step 5:** Fill in the form
```
First name:      John
Last name:       Doe
Designation:     Senior Developer
Email address:   john@company.com
Phone number:    555-1234
Photo:           (click "Choose File" and select an image)
```

**Step 6:** Click "Save"

**What happens:**
- Django inserts data into employee_employee table
- Photo is uploaded to media/images/ folder
- Employee ID is auto-generated
- created_at and updated_at are auto-set

**Result:** ✅ Employee is now in database!

### Method 2: Using Django Shell (Advanced)

Open Django shell:
```bash
python manage.py shell
```

Now type Python code:

```python
from employee.models import Employee

Employee.objects.create(
    first_name="Jane",
    last_name="Smith",
    designation="Product Manager",
    email_adress="jane@company.com",
    phone_number="555-5678"
)
```

**What this does:**
- Creates new Employee record
- Saves to database
- Auto-generates ID, timestamps
- Note: photo is optional here

Exit shell:
```python
exit()
```

### Verify Employee Was Created

```python
python manage.py shell
```

```python
from employee.models import Employee

# Get all employees
all_employees = Employee.objects.all()
for emp in all_employees:
    print(f"{emp.first_name} {emp.last_name} - {emp.designation}")

# Get one employee
john = Employee.objects.get(first_name="John")
print(john.email_adress)
```

Exit:
```python
exit()
```

---

## Tutorial 5: Viewing the Employee List

### What Happens Behind the Scenes

**Step 1:** User visits `http://127.0.0.1:8000/`

**Step 2:** Django URL router checks `mysite/urls.py`
```python
path('',views.home,name='home')  ← This matches!
```

**Step 3:** Django calls `mysite/views.py` → `home()` function
```python
def home(request):
    employee = Employee.objects.all()  # Get all employees
    context = {'employee': employee}
    return render(request, 'home.html', context)
```

**Step 4:** View queries database
```sql
SELECT * FROM employee_employee;
```

**Step 5:** Data passed to template in `context` dictionary
```python
{
    'employee': [
        <Employee: John Doe>,
        <Employee: Jane Smith>,
        <Employee: Mark Johnson>,
    ]
}
```

**Step 6:** Template `home.html` renders HTML
```html
{% for emp in employee %}
    <tr>
        <td>{{emp.first_name}} {{emp.last_name}}</td>
        <td>{{emp.designation}}</td>
        <td>{{emp.phone_number}}</td>
    </tr>
{% endfor %}
```

**Step 7:** HTML sent to browser

**Step 8:** User sees table with all employees

### Understanding the Template Loop

In `templates/home.html`:

```html
{% for emp in employee %}
    <!-- This block repeats for each employee -->
    <tr>
        <th scope="row">{{forloop.counter}}</th>  <!-- 1, 2, 3... -->
        <td>{{emp.first_name}}</td>              <!-- John, Jane, Mark... -->
        <td>{{emp.last_name}}</td>               <!-- Doe, Smith, Johnson... -->
        <td>{{emp.designation}}</td>             <!-- Developer, Manager... -->
        <td>{{emp.phone_number}}</td>            <!-- 555-1234, 555-5678... -->
    </tr>
{% endfor %}
```

**Special Variable `forloop.counter`:**
```
Iteration 1: forloop.counter = 1
Iteration 2: forloop.counter = 2
Iteration 3: forloop.counter = 3
```

This auto-numbers the rows!

### Modifying the Employee List

**Add a new column:**

Open `templates/home.html` and find:
```html
<th scope="col">Phone no</th>
```

Add after it:
```html
<th scope="col">Email</th>
```

Then add to table rows:
```html
<td>{{emp.email_adress}}</td>
```

**Result:** Email column appears in employee list!

---

## Tutorial 6: Viewing Employee Details

### How Employee Link Works

In `templates/home.html`:

```html
<a href="{% url 'employee:employee_details' emp.id %}">
    {{emp.first_name}} {{emp.last_name}}
</a>
```

**Breaking it down:**
- `<a>` = HTML link
- `href=` = where the link goes
- `{% url %}` = Django's URL resolver
- `'employee:employee_details'` = URL name with namespace
- `emp.id` = passes employee ID to the view

**Example:**
```
emp.id = 1
Generated URL: /employee/1/
```

### URL Routing Process

**Step 1:** User clicks on "John Doe" link

**Step 2:** Browser requests `/employee/1/`

**Step 3:** Django checks `mysite/urls.py`
```python
path('employee/',include('employee.urls',namespace='employee'))
```
Routes to `employee/urls.py`

**Step 4:** Django checks `employee/urls.py`
```python
app_name = 'employee'
urlpatterns = [
    path('<int:pk>/',views.employee_details,name='employee_details')
]
```
Matches `<int:pk>` with `pk=1`

**Step 5:** Django calls `employee/views.py` → `employee_details(request, pk=1)`

```python
def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {'employee': employee}
    return render(request, 'employee_details.html', context)
```

**Step 6:** View queries database
```sql
SELECT * FROM employee_employee WHERE id = 1;
```

**Step 7:** Data passed to template
```python
{
    'employee': <Employee: John Doe>
}
```

**Step 8:** Template renders employee details
```html
<img src="{{ employee.photo.url }}" alt="">
<p>Name: {{ employee.first_name }} {{ employee.last_name }}</p>
<p>Email: {{ employee.email_adress }}</p>
<p>Designation: {{ employee.designation }}</p>
<p>Phone: {{ employee.phone_number }}</p>
```

**Step 9:** User sees detailed employee card

### Back to Home Button

```html
<a href="{% url 'home' %}" class="btn btn-primary">Back to home</a>
```

**How it works:**
- `{% url 'home' %}` generates `/`
- Clicking button returns to employee list
- Process starts over (Tutorial 5)

---

## Tutorial 7: Managing Employees via Admin Panel

### Admin Panel URL

```
http://127.0.0.1:8000/admin/
```

### Logging In

1. Go to admin URL
2. Enter username and password
3. Click "Log in"

### Viewing Employees

1. Click "Employees" section
2. See list of all employees
3. Click on any employee to edit

### Adding New Employee

1. Click "Add Employee" button
2. Fill form fields
3. Upload photo (optional)
4. Click "Save"

### Editing Employee

1. Click on employee name
2. Modify fields
3. Click "Save"

### Deleting Employee

1. Click on employee name
2. Scroll down
3. Click "Delete" button at bottom
4. Confirm deletion

### Bulk Actions

**Select multiple employees:**
1. Check checkboxes next to employees
2. Select action from dropdown (e.g., "Delete selected")
3. Click "Go" button

### Customizing Admin Interface

In `employee/admin.py`:

```python
from django.contrib import admin
from .models import Employee

admin.site.register(Employee)
```

**Current state:** Basic admin interface

**Customize it:**

```python
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'designation', 'email_adress']
    list_filter = ['designation', 'created_at']
    search_fields = ['first_name', 'last_name', 'email_adress']
    list_per_page = 10
```

**What each line does:**
- `list_display` = columns shown in employee list
- `list_filter` = filter options on right side
- `search_fields` = searchable fields
- `list_per_page` = employees per page

---

## Tutorial 8: Customizing the Application

### Changing Page Title

In `templates/home.html`:

Find:
```html
<title>Document</title>
```

Change to:
```html
<title>Employee Management System</title>
```

### Changing Page Heading

In `templates/home.html`:

Find:
```html
<h1>Eemployee List</h1>
```

Change to:
```html
<h1>Our Team Members</h1>
```

### Changing Table Header

In `templates/home.html`:

Find:
```html
<th scope="col">First</th>
<th scope="col">Last</th>
<th scope="col">Handle</th>
```

Change to:
```html
<th scope="col">First Name</th>
<th scope="col">Last Name</th>
<th scope="col">Job Title</th>
```

### Adding CSS Styling

In `mysite/static/css/style.css`:

```css
/* Add custom colors */
body {
    background-color: #f5f5f5;
    font-family: Arial, sans-serif;
}

h1 {
    color: #333;
    text-align: center;
    margin-bottom: 30px;
}

table {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

a {
    color: #007bff;
    text-decoration: none;
    font-weight: bold;
}

a:hover {
    text-decoration: underline;
}
```

### Adding New Fields to Employee

**Step 1:** Edit `employee/models.py`

Find:
```python
class Employee(models.Model):
    # existing fields
```

Add new field:
```python
    department = models.CharField(max_length=100, default="General")
```

**Step 2:** Make migration

```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 3:** Update template

In `templates/home.html` add:
```html
<th scope="col">Department</th>
```

And in loop:
```html
<td>{{emp.department}}</td>
```

### Changing Background Color

In `templates/home.html`:

Find:
```html
<body>
```

Change to:
```html
<body style="background-color: #f0f0f0;">
```

### Hiding Employee Photo

In `templates/employee_details.html`:

Find:
```html
<img class="card-img-top" src="{{ employee.photo.url }}" alt="Card image cap">
```

Change to:
```html
<!-- <img class="card-img-top" src="{{ employee.photo.url }}" alt="Card image cap"> -->
```

---

## Troubleshooting Guide

### Problem 1: "Page Not Found" Error

**Error:** `Page not found (404)`

**Causes:**
- Wrong URL
- View not registered in urls.py
- Typo in URL pattern

**Solution:**
1. Check URL in browser matches a pattern in urls.py
2. Verify URL name is correct
3. Restart server with `Ctrl+C` then `python manage.py runserver`

---

### Problem 2: "Employee has no attribute photo"

**Error:** `AttributeError: 'Employee' object has no attribute 'photo'`

**Causes:**
- Employee created without photo field
- Pillow not installed

**Solution:**
```bash
pip install pillow
python manage.py migrate
```

---

### Problem 3: Image Not Displaying

**Error:** Image shows broken icon

**Causes:**
- Photo not uploaded
- Wrong image path
- Media files not configured

**Solution:**
1. Upload photo via admin panel
2. Check `settings.py` has:
   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```
3. Restart server

---

### Problem 4: "Reverse for 'employee_details' not found"

**Error:** `NoReverseMatch: Reverse for 'employee_details' not found`

**Causes:**
- Namespace not used
- app_name not set
- URL name doesn't match

**Solution:**
1. Check `employee/urls.py` has: `app_name = 'employee'`
2. Use full name: `{% url 'employee:employee_details' emp.id %}`
3. Check URL pattern name matches

---

### Problem 5: Port 8000 Already in Use

**Error:** `Error: That port is already in use.`

**Causes:**
- Another Django server running
- Another application using port 8000

**Solution:**
```bash
# Use different port
python manage.py runserver 8001

# Or find and kill process on 8000
netstat -ano | findstr :8000
```

---

### Problem 6: Virtual Environment Not Activating

**Error:** `env: The term 'env' is not recognized`

**Causes:**
- Not in correct directory
- env folder not created
- Wrong path

**Solution:**
1. Verify you're in project directory: `pwd` or `cd`
2. Check env folder exists: `ls env` or `dir env`
3. Use full path: `.\env\Scripts\Activate.ps1`

---

### Problem 7: Module Not Found Error

**Error:** `ModuleNotFoundError: No module named 'employee'`

**Causes:**
- App not in INSTALLED_APPS
- App not created

**Solution:**
1. Check `settings.py` contains: `'employee'` in INSTALLED_APPS
2. Verify `employee/` folder exists
3. Restart server

---

### Problem 8: Employee Data Disappears

**Error:** Added employees but they're gone after restart

**Causes:**
- Used test database
- Database file deleted
- Migration issues

**Solution:**
```bash
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```

---

## Quick Reference Commands

| Command | Purpose |
|---------|---------|
| `env\Scripts\Activate.ps1` | Activate virtual environment |
| `python manage.py runserver` | Start development server |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py makemigrations` | Create migrations from model changes |
| `python manage.py createsuperuser` | Create admin account |
| `python manage.py shell` | Open Python shell |
| `python manage.py collectstatic` | Collect static files for production |
| `deactivate` | Deactivate virtual environment |

---

## Practice Exercises

### Exercise 1: Add Department Field
1. Add `department` field to Employee model
2. Make migrations
3. Update templates to show department
4. Add at least 3 employees with different departments

### Exercise 2: Add Search Feature
1. Add search box in home.html
2. Filter employees by name in views.py
3. Display filtered results

### Exercise 3: Add Delete Button
1. Create delete view in employee/views.py
2. Add delete URL in employee/urls.py
3. Add delete button in employee_details.html
4. Delete employee functionality

### Exercise 4: Add Edit Feature
1. Create edit view in employee/views.py
2. Add edit URL in employee/urls.py
3. Create edit form template
4. Edit employee information

### Exercise 5: Add Sorting
1. Add sort dropdown in home.html
2. Modify home view to sort employees
3. Sort by: Name, Designation, Date Created

---

## Next Steps

After completing this tutorial:

1. **Add More Features**
   - Search functionality
   - Edit/Delete employee
   - Department management
   - Employee roles/permissions

2. **Improve UI/UX**
   - Add navigation menu
   - Improve styling with CSS
   - Add animations
   - Responsive design

3. **Deploy Application**
   - Use Heroku or Render
   - Set up PostgreSQL
   - Configure production settings

4. **Add Advanced Features**
   - User authentication
   - Employee login
   - Attendance tracking
   - Salary management

---

## Resources

- **Django Documentation:** https://docs.djangoproject.com/
- **Bootstrap Documentation:** https://getbootstrap.com/docs/
- **Python Documentation:** https://docs.python.org/3/
- **MDN Web Docs:** https://developer.mozilla.org/

---

## Support

If you encounter issues:

1. Check the **Troubleshooting Guide** above
2. Read error message carefully
3. Check official Django documentation
4. Search Stack Overflow
5. Ask in Django community forums

---

**Happy Learning! 🎉**

**Last Updated:** November 20, 2025  
**Django Version:** 5.2.8  
**Python Version:** 3.11.0
