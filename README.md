Projet E-Commerce avec Django, Docker, CI/CD, AWS EC2 et S3
Description
Ce projet implémente une plateforme e-commerce simple avec Django, utilisant une base de données SQLite pour stocker les informations sur les produits, les utilisateurs et les commandes. Le projet est containerisé avec Docker et bénéficie d'une pipeline CI/CD via GitHub Actions pour un déploiement automatisé sur AWS EC2, avec le stockage des fichiers statiques sur Amazon S3.

Fonctionnalités
Gestion des produits : Ajouter, modifier et supprimer des produits.
Panier d'achat : Les utilisateurs peuvent ajouter des produits au panier, les visualiser et les supprimer.
Authentification des utilisateurs : Inscription, connexion, et gestion des sessions utilisateur.
Gestion des commandes : Finalisation des commandes avec un système simple de suivi.
Interface utilisateur : Interface frontend simple pour la navigation dans le catalogue, l'ajout au panier, et la validation des commandes.
Technologies utilisées
Backend : Django (Python)
Base de données : SQLite
Containerisation : Docker
CI/CD : GitHub Actions
Frontend : Templates Django (HTML, CSS, JS)
Stockage statique : Amazon S3
Déploiement : AWS EC2 (Elastic Compute Cloud)
Prérequis
Avant de démarrer, assurez-vous d'avoir les éléments suivants installés :

Docker
Git
AWS CLI
Un compte GitHub (pour GitHub Actions)
Un compte AWS pour la gestion des services EC2 et S3.
