import requests
from bs4 import BeautifulSoup
from scrap_book import scrap_one_book
import csv
import os
import re
import wget

# Fonction pour nettoyer les noms de fichiers
def sanitize_filename(filename):
    name = re.sub(r'[<>:"/\\|?*]', '_', filename)
    temp = ""
    for carac in name :
        if carac == ' ' :
            carac = '_'
        temp = temp + carac
    name = temp
    return name

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
    for i in range (nb_next+1): # +1 pour inclure la dernière page
        if i == 0:
            url = url_cat
        else:
            url_categorie = url_cat.replace("index.html","page-")
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

def creation_of_files(nom_category):
    # creation des dossiers
    # répertoire de travail actuel
    cwd = os.getcwd()
    # dossier output
    file = os.path.join(cwd, "output")
    os.makedirs(file, exist_ok=True)
    # Sous-répertoire pour la catégorie
    file_category = os.path.join(file, nom_category)
    os.makedirs(file_category, exist_ok=True)
    # Chemin pour enregistrer le fichier CSV
    file_save = os.path.join(file_category, f"extrait_informations_{nom_category}.csv")
    # Sous-répertoire pour les images
    file_img = os.path.join(file_category, "img")
    os.makedirs(file_img, exist_ok=True)
    return file_save,file_img
    
def data_recording(url_categoy,file_save):
    category_books_dicts = data_recovery(url_categoy)
    # enregistrement des données
    with open(file_save, 'w', newline='',encoding="utf-8") as fichier:
        # Get the field names from the keys of the first dictionary
        fieldnames = category_books_dicts[0].keys()
        # Create a writer object
        writer = csv.DictWriter(fichier,delimiter=";", fieldnames=fieldnames)
        # Write the header row
        writer.writeheader()
        # Write the rows of data
        writer.writerows(category_books_dicts)

def data_recovery(url_categoy):
    books_links = category_books_link(url_categoy)
    category_books_dicts = []
    # récuperation des données
    for book_link in books_links:
        book_url = "https://books.toscrape.com/catalogue/" + book_link
        book_dict = scrap_one_book(book_url)
        category_books_dicts.append(book_dict)
    return category_books_dicts

def download_image (url_categoy,file_img):
    category_books_dicts = data_recovery(url_categoy)
    urls_img = [d["image_url"] for d in category_books_dicts]
    title_book = [d["title"] for d in category_books_dicts]
    t = 0
    for url in urls_img: 
        image_name = title_book[t]
        output_path = os.path.join(file_img,sanitize_filename(image_name)+".jpg")
        response = requests.get(url, stream=True)
        if response.status_code == 200:  # Vérifier si la requête a réussi
            wget.download(url, out = output_path)
        t = t+1

def scrap_category(nom_category, url_categoy):
    file = creation_of_files(nom_category)
    data_recording(url_categoy,file[0])
    download_image(url_categoy,file[1])


if __name__ == "__main__":
    nom = input ("Entrer le nom de la catégorie à scraper : ")
    url = input("Entrer le lien de la catégorie à scraper : ")
    scrap_category (nom,url)



