#!/bin/sh
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn --workers 3 --bind 0.0.0.0:8080 ecommerce.wsgi:application