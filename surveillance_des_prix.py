import requests
from bs4 import BeautifulSoup
import csv



#recuperation des informations du livre
def scrap_one_book(url, doc):
    reponse = requests.get(url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, "html.parser")
        product_page_url = url
        universal_product_code = soup.find('table', class_ ='table table-striped' ).find(string="UPC").find_parent('tr').find('td').text.strip()
        title = soup.find('li',class_ ='active' ).text
        price_including_tax = soup.find('table', class_ ='table table-striped' ).find(string="Price (incl. tax)").find_parent('tr').find('td').text.strip()[1:]
        price_excluding_tax =soup.find('table', class_ ='table table-striped' ).find(string="Price (excl. tax)").find_parent('tr').find('td').text.strip()[1:]
        number_available =  soup.find('table', class_ ='table table-striped' ).find(string="Availability").find_parent('tr').find('td').text.strip()
        product_description = soup.find('div', id ='product_description').find_next('p').text.strip()
        category = soup.find('ul', class_ = 'breadcrumb' ).find('li', class_='active').find_previous('a').text.strip()
        review_rating = soup.find('table', class_ ='table table-striped' ).find(string="Number of reviews").find_parent('tr').find('td').text.strip()
        image_url = soup.find('img').get('src')
        print (product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url)
    #ecrire les informations dans le ficheri csv
    doc.writerow([product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url])


#nombre de pages de la catégorie choisi
def nb_page(nb,url_cat):
    next = 0
    for i in range (1,nb):
        url_categorie = url_cat
        url = url_categorie+str(i)+".html"
        reponse = requests.get(url)
        if reponse.ok:
            next += 1
    return next


#lien vers les livres d'une catégorie
def link_book(nb_next,url_cat):   
    for i in range (nb_next) : 
        url = url_cat+str(i)+".html"
        reponse = requests.get(url)  
        if reponse.ok:            
            soup = BeautifulSoup(reponse.text, "html.parser") 
            # récupérer url d'une page d'une catégorie
            livres = soup.find_all("h3")
            for livre in livres :
                link = livre.find("a")["href"]
                link_ok = BeautifulSoup(link, "html.parser").text.strip('../../../')
                lien_livre.append(link_ok)
    return lien_livre
    


if __name__ == "__main__" :
    #list url
    lien_livre = []
    url_categorie = "https://books.toscrape.com/catalogue/category/books/young-adult_21/page-"
    next=nb_page(20,url_categorie)+1
    link_book(next,url_categorie)

    # ouverture en écriture du fichier
    with open('extrait_informations.csv', 'w', newline='',encoding="utf-8") as fichier:
        ecrire = csv.writer(fichier)
        #ecriture des colonnes
        ecrire.writerow(['product_page_url','universal_ product_code (upc)','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url'])
        
        for i in lien_livre : 
            url = "https://books.toscrape.com/catalogue/"+str(i)
            scrap_one_book(url,ecrire)


