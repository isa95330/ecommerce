<<<<<<< HEAD
# Use Python 3.11
FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies (if needed)
=======
# Dockerfile

# Utilisation de Python 3.11 comme base
FROM python:3.11-slim-buster

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système (si nécessaire)
>>>>>>> main
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

<<<<<<< HEAD
# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY src/ /app/src/
=======
# Copier le fichier requirements.txt dans l'image
COPY requirements.txt /app/requirements.txt

# Mettre à jour pip et installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier le reste des fichiers du projet dans l'image
COPY . /app/
>>>>>>> main
