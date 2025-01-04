import requests
from bs4 import BeautifulSoup
import re

# recuperation des informations du livre
def scrap_one_book(url):
    reponse = requests.get(url)
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.content, 'lxml')
        product_page_url = url
        universal_product_code = soup.find('table', class_ ='table table-striped' ).find(string="UPC").find_parent('tr').find('td').text.strip()
        title = soup.find('li',class_ ='active' ).text
        price_including_tax = soup.find('table', class_ ='table table-striped' ).find(string="Price (incl. tax)").find_parent('tr').find('td').text
        price_including_tax = re.sub(r"[£Â£]", "", price_including_tax)
        price_excluding_tax =soup.find('table', class_ ='table table-striped' ).find(string="Price (excl. tax)").find_parent('tr').find('td').text
        price_excluding_tax = re.sub(r"[£Â£]", "", price_excluding_tax)
        number_available =  soup.find('table', class_ ='table table-striped' ).find(string="Availability").find_parent('tr').find('td').text.strip()
        number_available = int(number_available.split('(')[1].split()[0]) 
        category = soup.find('ul', class_ = 'breadcrumb' ).find('li', class_='active').find_previous('a').text.strip()
        review_rating = soup.find('p', class_ = 'star-rating').get("class")[1]
        image_url = soup.find('img').get('src').replace("../../", "https://books.toscrape.com/")
        product_description = soup.find('div', id ='product_description')
        if product_description != None:
            product_description = soup.find('div', id ='product_description').find_next('p').text.strip()
        else: 
            pass

    book_info = {
       "product_page_url": product_page_url,
       "universal_product_code": universal_product_code,
       "title": title,
       "price_including_tax": price_including_tax,
       "price_excluding_tax": price_excluding_tax,
       "number_available": number_available,
       "product_description": product_description,
       "category": category,
       "review_rating": review_rating,
       "image_url": image_url
    }
    return book_info

if __name__ == "__main__":
    url = input("Entrer le lien du livre à scraper : ")
    book = scrap_one_book(url)
    print(book)