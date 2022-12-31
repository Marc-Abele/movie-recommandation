# OUTILS
import bs4
import requests
from bs4 import BeautifulSoup



# fonction pour scraper l'affiche du film
def affiche(id_film):
    link = 'https://www.imdb.com/title/' + id_film
    reponse = requests.get(link, 
                       headers={"Accept-Language":"fr-FR", 
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"})
    soup = BeautifulSoup(reponse.content , "html.parser")
    affiche = soup.find('img', {'class' : 'ipc-image'})
    try:
        return (affiche['src'])
    except:
        pass

# fonction pour scraper le titre en français
def title(id_film):
    link = 'https://www.imdb.com/title/' + id_film
    reponse = requests.get(link, 
                       headers={"Accept-Language":"fr-FR", 
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"})
    soup = BeautifulSoup(reponse.content , "html.parser")
    title = soup.find('div', attrs = {'class' : 'sc-80d4314-1 fbQftq'})
    return title.h1.text

# fonction pour scraper le synopsis
def synopsis(id_film):
    link = 'https://www.imdb.com/title/' + id_film
    reponse = requests.get(link, 
                       headers={"Accept-Language":"fr-FR", 
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"})
    soup = BeautifulSoup(reponse.content , "html.parser")
    synopsis = soup.find_all('span', attrs = {'role' : 'presentation'})
    try :
        return synopsis[-1].text
    except AttributeError:
        return ('Pas de synopsis')

# fonction pour scraper le pays d'origine
def pays(id_film):
    link = 'https://www.imdb.com/title/' + id_film
    reponse = requests.get(link, 
                       headers={"Accept-Language":"fr-FR", 
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"})
    soup = BeautifulSoup(reponse.content , "html.parser")
    title = soup.find('li', attrs = {'role': 'presentation', 
                                     'class' : 'ipc-metadata-list__item',
                                     'data-testid' : 'title-details-origin'})
    try:
        return title.div.ul.li.a.text
    except AttributeError:
        return 'Pays inconnu'