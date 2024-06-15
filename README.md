## Create virtual env
python3 -m venv name-of-env

## activate virtual env
source name-of-env/bin/activate
# ‘deactivate’ to deactivate env

## installing Django
pip3 install Django

## see Django commands
django-admin

## create project
cd name-of-env
django-admin startproject name-of-project

## run project
cd name-of-project
python manage.py runserver

## create app
python manage.py startapp name-of-app
