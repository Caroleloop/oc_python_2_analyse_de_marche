import requests
from bs4 import BeautifulSoup
import csv



# ouverture en écriture du fichier
with open('extrait_informations.csv', 'w', newline='',encoding="utf-8") as fichier:
    ecrire = csv.writer(fichier)

    #ecriture des colonnes
    ecrire.writerow(['product_page_url','universal_ product_code (upc)','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url'])


    # choix du livre
    url = 'http://books.toscrape.com/catalogue/set-me-free_988/index.html'

    reponse = requests.get(url)

    #recuperation des informations du livre
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
    ecrire.writerow([product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url])



        
