import requests
from bs4 import BeautifulSoup
import csv




    
#liste des liens des catégories
def lien_categorie ():
    liste_cat = []
    liste_cat_ok = []
    url = "https://books.toscrape.com/index.html"
    reponse = requests.get(url)  
    if reponse.ok:            
        soup = BeautifulSoup(reponse.text, "html.parser") 
        categorie = soup.find("div",class_ = "side_categories").find_all("li")        
        for cat in categorie :
            link = cat.find("a")["href"]
            liste_cat.append(link)
        for i in liste_cat :
            i = i.replace("index.html","page-")
            liste_cat_ok.append(i)
    del liste_cat_ok[0:1]
    return(liste_cat_ok)

#liste des catégories
def nom_categorie (liste):
    nom_cat =[]
    for i in liste :
        i = i.replace("catalogue/category/books/","")
        i = i.split("_")[0]
        nom_cat.append (str(i))
    return nom_cat




if __name__ == "__main__" :
    # lien_des_livres = link_book(1,"https://books.toscrape.com/catalogue/category/books/travel_2/page-")
    # print(lien_des_livres)
    liste_categorie = lien_categorie()
    list_nb_page=[]
    # nom= []
    nom = nom_categorie (liste_categorie)
    # print(nom)
    # for n in nom : 
    #     print(n)
    b=0
    for i in liste_categorie :
            # print(i)
            # nom = nom_categorie (liste_categorie)
            n= nom[b]
            # print (n)
            url_categorie = "https://books.toscrape.com/"+i
            # print(url_categorie)
            # for j in url_categorie:
            #     print(j)
            next=nb_page(url_categorie)
            # print(next)
            list_nb_page.append(next)
            # print(list_nb_page)
            for n in list_nb_page :
                lien_des_livres = link_book(next,url_categorie)
                # print(lien_des_livres)
            # print('')
            # print('')
                ecrire(n)
            b = b+1
            break
                    

    