# TP1 - Git & Environnement MLOps

## Description

Ce projet a pour objectif de mettre en place un environnement de travail reproductible pour un projet MLOps.

## Environnement

- Python 3.10
- Pandas
- Scikit-learn
- python-dotenv
- IPykernel

## Gestion de l'environnement

L'environnement principal est défini dans :

`environment.yml`

Un export complet est disponible dans :

`environment-full.yml`

## Test

Le fichier `test_env.py` permet de vérifier :

- la version de Python
- Pandas
- Scikit-learn
- le chargement des variables d'environnement

## Git

Le projet utilise Git avec GitHub.

Branches utilisées :

- `main`
- `feature/test`

## Sécurité

Les variables sensibles sont stockées dans `.env`.

Le fichier `.env` est exclu du dépôt grâce à `.gitignore`.