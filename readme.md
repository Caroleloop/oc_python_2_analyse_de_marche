# Système de surveillance des prix pour Books to Scrape.


Ce document présente comment exécuter les différents programmes qui sert à scraper des informations sur des livres du site Books to scrape.


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

Ces données sont enregistrées dans un fichier CSV et les image des couvertures sont aussi enregistrée dans un dossier "img".


### Pré-requis

Il faut utiliser la dernière version de Python que vous pourrez retrouver sur le site officiel de Python : https://www.python.org/downloads/


### Installation

Dans un terminal faire les étapes suivantes.

1.1 Cloner le dépôt git dans le dossier de travail
       a. Aller sur la page : https://github.com/Caroleloop/oc_python_2_analyse_de_marche
       b. Pour le reste de la procédure, veuillez vous référer à la documentation git: https://docs.github.com/fr/repositories/creating-and-managing-repositories/cloning-a-repository

1.2 Création d'un environement virtuelle
        a. Placez vous dans le dossier courant
        b. Créez votre environnement virtuel  
                    python -m venv <your-virtual-env-name>
1.3 Activer l'enviremenet virtuelle
                    <your-virtual-env-name>\Scripts\activate.bat (sous Windows)
                ou  source <your-virtual-env-name>/bin/activate (sous Mac/Linux)
1.4 Installation des packages
                    pip install -r requirements.txt


## Démarrage

Dites comment faire pour lancer votre projet


## Fabriqué avec

Entrez les programmes/logiciels/ressources que vous avez utilisé pour développer votre projet

_exemples :_
* [Materialize.css](http://materializecss.com) - Framework CSS (front-end)
* [Atom](https://atom.io/) - Editeur de textes

## Contributing

Si vous souhaitez contribuer, lisez le fichier [CONTRIBUTING.md](https://example.org) pour savoir comment le faire.

## Versions

**Dernière version stable :** 5.0
**Dernière version :** 5.1
Liste des versions : [Cliquer pour afficher](https://github.com/your/project-name/tags)
_(pour le lien mettez simplement l'URL de votre projets suivi de ``/tags``)_


## Auteurs

* **Carole Roch** _alias_ [@Caroleloop](https://github.com/Caroleloop)



