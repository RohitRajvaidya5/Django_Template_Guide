
# 🧩 Django: Template and Static File Setup Guide

This README is designed to help developers quickly set up and integrate HTML templates and static files (CSS, JS, images) into a Django project.

---

## 📦 1. Create a Django Project

Use the following command to start a new Django project:

```bash
django-admin startproject project_name
```

---

## 🧪 2. First Steps with Views (Without Templates)

Before integrating templates, you can test your views using `HttpResponse`:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

---

## ⚙️ 3. Setting Up Templates

### 🗂️ Step 1: Create a `Templates` Folder

- Create a folder named `Templates` in the **root directory** (same level as `manage.py`).
- Place your HTML files here (e.g., `index.html`).

### 🧾 Step 2: Configure `settings.py`

```python
import os

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'Templates')],
        ...
    }
]
```

---

## 🗃️ 4. Recommended Project Structure

```python
project_root/
│
├── manage.py
├── db.sqlite3
├── project_name/       # Contains settings.py, urls.py
├── Templates/          # HTML templates here
│   └── index.html
└── static/             # Static files (CSS, JS, Images)
    └── style.css
```

---

## 🎨 5. Adding Static Files

### Step 1: Configure `settings.py`

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

### Step 2: Load Static Files in Templates

- Add at the **top** of your HTML file:
  
```django
{% load static %}
```

- Link a CSS file using:
  
```html
<link rel="stylesheet" href="{% static 'style.css' %}">
```

---

## 🧠 6. Using Templates in Views

Use Django's `render()` function to serve templates:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
```

---

## ✅ Summary Checklist

- [ ] Create `Templates/` and `static/` folders in the root directory.
- [ ] Configure `TEMPLATES['DIRS']` in `settings.py`.
- [ ] Configure `STATICFILES_DIRS` in `settings.py`.
- [ ] Use `{% load static %}` and `{% static 'file' %}` in templates.
- [ ] Use `render()` to return templates from views.

---

## Creating a New Django App with Template & Extends

### 1. Create a New App

Use the following command to create a new Django app:

```bash
django-admin startapp <app_name>
```

---

### 2. Template Folder Setup (Two Options)

You can choose one of the following options to add the `templates` folder:

**Option 1:**  
Add the `templates` folder inside the **project root folder**.

```path
project_root/
    templates/
        your_templates_here/
```

**Option 2:**  
Insert the `templates` folder inside the **app folder**.

```path
app_name/
    templates/
        app_name/
            your_templates_here/
```

Make sure your Django settings are updated to look for templates in the correct directories.

---

### 3. URL Configuration

- Add a `urls.py` file in the **app folder**.
- In **project root `settings.py`**:
  - Add the app name to `INSTALLED_APPS`.
- In **project root `urls.py`**:
  - Include the app’s `urls.py` using `include()`.

```python
# project/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_name/', include('app_name.urls')),
]
```

---

### 4. Template and Static File Access

- Ensure the `DIRS` option in the `TEMPLATES` setting includes the correct template paths.
- Django will fetch:
  - Templates from either the **app’s `templates` folder** or the **root `templates` folder**.
  - Static files from the configured `static/` folders.

```python
# settings.py
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
```

---

### 5. Add Shared Templates (e.g., Navbar)

- Add commonly used HTML files like `navbar.html` inside the **project root `templates/` folder**.

**Folder Structure Example:**

```path
project_root/
│
├── project/
│   └── settings.py
│
├── templates/
│   ├── navbar.html
│   └── another_template.html
```

**Remaining Structure:**

```path
static/
app_name/
├── templates/
│   └── app_name/
│       └── html_files_here.html
```

---

### ✅ Notes

- Always use app-specific folders inside `templates/` to avoid conflicts.
- Don't forget to load static files in your HTML using `{% load static %}` and set up the `STATICFILES_DIRS` if needed.

---

Happy Coding! 🚀
