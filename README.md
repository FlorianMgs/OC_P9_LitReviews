# OC_P9_LitReviews
Projet réalisé dans le cadre de ma formation OpenClassrooms Développeur d'Applications Python.  
Il s'agit d'une application web réalisée avec Django pour une société fictive, LitReviews.  
L'application est un réseau social permettant de demander et poster des critiques de livres.

## Features

* Inscription / connexion.
* Consulter un flux personnalisé en fonction de ses abonnements.
* Consulter un flux "Découvertes" répertoriant toutes les demandes et critiques.
* Trier les demandes et critiques sur chacune des pages les affichant.
* Publier des demandes de critique.
* Publier des critiques en réponse à une demande ou pas en réponse.
* Modifier / supprimer ses demandes et critiques.
* Consulter son profil, ses abonnements, changer sa photo de profil.
* Consulter le profil et les abonnements d'un autre ustilisateur.
* S'abonner / se désabonner d'un autre utilisateur.
* Rechercher un utilisateur.

## Installation & lancement

Commencez tout d'abord par installer Python 3.10.  
Si vous souhaitez modifier le style, il est préférable d'installer Sass plutôt que d'éditer directement static/css/style.css.  
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/FlorianMgs/OC_P9_LitReviews.git
```
Placez vous dans le dossier OC_P9_LitReviews, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Il ne reste plus qu'à installer les packages requis:
```
pip install -r requirements.txt
```
Ensuite, placez vous à la racine du projet (là ou se trouve le fichier manage.py), puis effectuez les migrations:
```
python manage.py makemigrations
```
Puis: 
```
python manage.py migrate
```
Il ne vous reste plus qu'à lancer le serveur: 
```
python manage.py runserver
```
Vous pouvez ensuite utiliser l'applicaton à l'adresse suivante:
```
http://127.0.0.1:8080
```
