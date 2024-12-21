import requests
from bs4 import BeautifulSoup
from scrap_category import scrap_category


#liste des liens des catégories
def links_categories ():
    links_cat = []
    links_categories = []
    url = "https://books.toscrape.com/index.html"
    reponse = requests.get(url)  
    if reponse.ok:            
        soup = BeautifulSoup(reponse.text, "html.parser") 
        categorie = soup.find("div",class_ = "side_categories").find_all("li")        
        for cat in categorie :
            link = cat.find("a")["href"]
            links_cat.append(link)
        for link in links_cat:
            links = "https://books.toscrape.com/" + link
            links_categories.append(links)
    del links_categories[0:1]
    return links_categories

#nom des catégories
def name_category (liste):
    name_cat =[]
    for name in liste :
        name = name.replace("https://books.toscrape.com/catalogue/category/books/","")
        name = name.split("_")[0]
        name_cat.append (str(name))
    return name_cat

def scrap_all_categories ():
    links = links_categories()
    names = name_category(links)
    for name, link in zip(names, links): 
        resultat = scrap_category(name, link)
    return resultat

if __name__ == "__main__":
    scrap_all_books = scrap_all_categories()

   

    