# Utilisation de Python 3.11 comme base
FROM python:3.11-slim-buster

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE "ecommerce.settings"

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système (si nécessaire)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier requirements.txt dans l'image
COPY requirements.txt /app/requirements.txt

# Mettre à jour pip et installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet dans l'image
COPY . /app/

# Rendre le script entrypoint.sh exécutable
RUN chmod +x /app/entrypoint.sh

# Définir la commande pour démarrer l'application
ENTRYPOINT ["/app/entrypoint.sh"]
