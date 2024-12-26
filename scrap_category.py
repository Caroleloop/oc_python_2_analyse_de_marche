import requests
from bs4 import BeautifulSoup
from scrap_book import scrap_one_book
import csv
import os
import re

# Fonction pour nettoyer les noms de fichiers
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', ',', filename)


#nombre de pages de la catégorie choisi
def nb_page(url_cat):
    next = 0
    i=1
    url_categorie = url_cat.replace("index.html","page-")
    while True : 
        url = url_categorie+str(i)+".html"
        reponse = requests.get(url)
        if reponse.ok:
            next += 1
        else:
            break
        i += 1
    return next

#lien vers les livres d'une catégorie
def category_books_link(url_cat):
    nb_next = nb_page(url_cat)
    liens_livres = []
    if nb_next == 0:
        url = url_cat
        reponse = requests.get(url)  
        if reponse.ok:            
            soup = BeautifulSoup(reponse.text, "html.parser") 
            # récupérer url d'une page d'une catégorie
            livres = soup.find_all("h3")
            for livre in livres :
                link = livre.find("a")["href"]
                link_ok = BeautifulSoup(link, "html.parser").text.strip('../../../')
                liens_livres.append(link_ok)
    else: 
        url_categorie = url_cat.replace("index.html","page-")
        for i in range (nb_next) : 
            url = url_categorie+str(i+1)+".html"
            reponse = requests.get(url)  
            if reponse.ok:            
                soup = BeautifulSoup(reponse.text, "html.parser") 
                # récupérer url d'une page d'une catégorie
                livres = soup.find_all("h3")
                for livre in livres :
                    link = livre.find("a")["href"]
                    link_ok = BeautifulSoup(link, "html.parser").text.strip('../../../')
                    liens_livres.append(link_ok)
    return liens_livres

# ouverture en écriture du fichier
def scrap_category(nom_category, url_categoy):
    books_links = category_books_link(url_categoy)
    category_books_dicts = []

    #ceation des dossiers
    # Chemin principal
    file = os.path.join("C:\\Formation\\Projet_02\\repo\\output")
    os.makedirs(file, exist_ok=True)
    # Sous-répertoire pour la catégorie
    file_category = os.path.join(file, nom_category)
    os.makedirs(file_category, exist_ok=True)
    # Chemin pour enregistrer le fichier CSV
    file_save = os.path.join(file_category, f"extrait_informations_{nom_category}.csv")
    # Sous-répertoire pour les images
    file_img = os.path.join(file_category, "img")
    os.makedirs(file_img, exist_ok=True)
    
    #récuperation des données
    for book_link in books_links:
        book_url = "https://books.toscrape.com/catalogue/" + book_link
        book_dict = scrap_one_book(book_url)
        category_books_dicts.append(book_dict)

    #enregister des images
    urls_img = [d["image_url"] for d in category_books_dicts]
    title_book = [d["title"] for d in category_books_dicts]
    t = 0
    for url in urls_img: 
        url_modifie = url.replace("../../", "")
        url_img = "https://books.toscrape.com/"+url_modifie
        image_name = title_book[t]
        # output_path = os.path.join(file_img, image_name)
        output_path = os.path.join(file_img,sanitize_filename(image_name))
        response = requests.get(url_img, stream=True)
        if response.status_code == 200:  # Vérifier si la requête a réussi
            with open(output_path, "wb") as file:
                for chunk in response.iter_content(1024):  # Télécharger par morceaux
                    file.write(chunk)
        t = t+1

    #enregistrement des données
    with open(file_save, 'w', newline='',encoding="utf-8") as fichier:
        # Get the field names from the keys of the first dictionary
        fieldnames = category_books_dicts[0].keys()
        
        # Create a writer object
        writer = csv.DictWriter(fichier,delimiter=";", fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Write the rows of data
        writer.writerows(category_books_dicts)



if __name__ == "__main__":
    nom = "Mystery"
    url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    scrap_category (nom,url)



