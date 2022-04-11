from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest

page_n = 1

url = "https://www.ouedkniss.com/velo_loisirs_divertissements-r"
response = requests.get(url)

velo_titre = []
velo_prix = []
velo_lien = []

while(True):

    content     = response.content
    soup        = BeautifulSoup(content, "lxml")    
    products    = soup.find_all("ul", {'class': 'annonce_left'})

    
    try:
        
        for p in range(len(products)):

            velo_titre.append(products[p].find('h2').text)

            if products[p].find('span',  itemprop="price") != None:

                velo_prix.append(products[p].find('span',  itemprop="price").text)
            else:
                velo_prix.append("None")

            velo_lien.append("https://www.ouedkniss.com/"+products[p].find('a')['href'])
    except:
        
        break
    
    page_n = page_n + 1
    
    if( page_n == 100):
        break

    url = f"https://www.ouedkniss.com/velo_loisirs_divertissements-r/{page_n}"
    response = requests.get(url)



file_lists = [velo_titre, velo_prix, velo_lien]
infos = zip_longest(*file_lists)

with open("/home/lakhdar/Desktop/vélo_oued.csv", "w") as myfrile:
    wr = csv.writer(myfrile)
    wr.writerow(["titre", "prix", "lien"])
    wr.writerows(infos)
