import requests
from bs4 import BeautifulSoup
from scrap_book import scrap_one_book
import csv
from pathlib import Path

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

    #ceeation des dossiers
    file = Path("C:\\Formation\\Projet_02\\repo\\output")
    file.mkdir(exist_ok=True)
    file_category = Path(file / nom_category)
    file_category.mkdir(exist_ok=True)
    file_save = file_category / f"extrait_informations_{nom_category}.csv"
    
    #récuperation des données
    for book_link in books_links:
        book_url = "https://books.toscrape.com/catalogue/" + book_link
        book_dict = scrap_one_book(book_url)
        category_books_dicts.append(book_dict)

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



