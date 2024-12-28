# Système de surveillance des prix pour Books to Scrape.


Ce document présente comment exécuter les différents programmes qui servent à scraper des informations sur des livres du site Books to scrape.


## Pour commencer

Les programmes servent à scraper les livres. Le premier programme sert à scraper un livre, le second une catégorie de livre et le dernier l'ensemble du site Books to scape. Différentes informations sont extraites sur les livres : 

+ Product page url
+ Universal product code
+ Title
+ Price including tax
+ Price excluding tax
+ Number available
+ Product description
+ Category
+ Review rating
+ Image url

Ces données sont enregistrées dans un fichier CSV et les images des couvertures sont aussi enregistrées dans un dossier "img".


### Pré-requis

Il faut utiliser la dernière version de Python que vous pourrez retrouver sur le site officiel de Python : https://www.python.org/downloads/


### Installation

Dans un terminal faire les étapes suivantes :

1.1 Cloner le dépôt git dans le dossier de travail

+ Aller sur la page : https://github.com/Caroleloop/oc_python_2_analyse_de_marche
+ Pour le reste de la procédure, veuillez vous référer à la documentation git: https://docs.github.com/fr/repositories/creating-and-managing-repositories/cloning-a-repository


1.2 Création d'un environement virtuel

+ Placez vous dans le dossier courant

+ Créez votre environnement virtuel

                    
                    python -m venv <your-virtual-env-name>
                    

1.3 Activer l'environnement virtuel

                    
                    <your-virtual-env-name>\Scripts\activate.bat (sous Windows)
                    

ou 

                    
                    source <your-virtual-env-name>/bin/activate (sous Mac/Linux)
                    

1.4 Installation des packages

                    
                    pip install -r requirements.txt
                    



## Démarrage

### 1.Scraper un livre

Pour scraper un livre, vous devez utiliser le programme "scrap_book.py".

Lancer le programme.

Il vous sera demandé d'entrer le lien du livre à scraper.

Dans le dossier "scraper_ un_livre", qui se trouve dans le dossier "output" vous aurez un dossier avec le titre du livre. 

Dans ce dossier vous trouverez un fichier CSV ainsi qu'un dossier img avec l'image de la couverture du livre dedans.



### 2.Scraper une catégorie

Pour scraper une catégorie, vous devez utiliser le programme "scrap_category.py".

Lancer le programme.

Il vous sera demandé d'entrer le nom de la catégorie à scraper, puis d'entrer le lien de la catégorie à scraper à scraper.

Dans le dossier "output", vous trouverez un dossier avec le nom de le catégorie scraper. 

Dans ce dossier vous trouverez un fichier CSV ainsi qu'un dossier img avec les images des couvertures des livres dedans.



### 3.Scraper tout le site

Pour scraper le site, vous devez utiliser le programme "scrap_all_categories.py".

Lancer le programme.

Dans le dossier "output", vous trouverez un dossier pour chaque catégorie. 

Dans ce dossier vous trouverez un fichier CSV ainsi qu'un dossier img avec les images des couvertures des livres dedans.




## Utilisation des données

Les fichiers CSV peuvent être ouvert dans Excel.

Pour cela, ouvrez Excel puis aller dans l'onglet "Données". 

Ouvrez les fichiers avec "A partir d'un fichier texte/CSV".

Une fenêtre s'ouvrira, dans "Détection du type de données" mettez "Selon le jeu de données complet" pour avoir toutes les données.

Puis appuyez sur "Charger".

Ainsi vous pourrez utiliser les données.


## Auteurs

* **Carole Roch** _alias_ [@Caroleloop](https://github.com/Caroleloop)



