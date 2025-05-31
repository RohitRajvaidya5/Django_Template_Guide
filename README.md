
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

Happy Coding! 🚀
