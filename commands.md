# Packages

Django

python-dotenv 1.0.0

djangorestframework==3.14.0

pytest==7.4.2

pytest-django==4.5.2

django-mptt==0.15.0

# Commands

django-admin startproject DjangoDRFeCommerceProject

python -m venv venv

venv/Scripts/activate

python manage.py runserver

from django.core.management.utils import get_random_secret_key 

print(get_random_secret_key())  

pip freeze > requirements.txt   

pip install python-dotenv

pip install djangorestframework

pip install pytest

pip install pytest-django

python manage.py startapp product .\DjangoDRFeCommerceProject\product\

pip install django-mptt

python manage.py makemigrations

Python manage.py migrate

# Pytest

pytest -h