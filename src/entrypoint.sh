#!/bin/sh

# Synchroniser les fichiers statiques depuis S3
aws s3 sync s3://ecom-bucket-unique123/static /app/static

# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate --noinput

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Démarrer le serveur Gunicorn
exec gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8080
