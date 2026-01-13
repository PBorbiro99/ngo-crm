# NGO Management System (CRM)

**Student:** Stefaniga Sebastian  
**Course:** Web Technologies - UVT  

## What it does
Web-based CRM for NGOs to manage donors, projects, volunteers, and events.

## Tech Stack
- Django 5.x + Django REST Framework
- HTML5, CSS, JavaScript
- SQLite Database

## Setup
```bash
cd ngo-crm
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework django-cors-headers pillow python-decouple
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## Features
- REST API with CRUD operations
- User authentication (Admin/Staff/Volunteer roles)
- Donor & donation tracking
- Project management
- Volunteer coordination
- Event planning
