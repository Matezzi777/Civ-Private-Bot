import requests
import sqlite3
from bs4 import BeautifulSoup

LANG = ["", "/de", "/es", "/fr", "/it", "/pl", "/pt-BR", "/ru"]
URL_BASE = "https://www.civilopedia.net"

#Retourne le code HTML d'une page web à partir de son url
def get_html(url : str):
    response = requests.get(url)
    return (response.text)

def extract_urls_from_html(html):
    connexion = sqlite3.connect('civilopedia.sqlite')
    cursor = connexion.cursor()
    req : str = f""
    cursor.execute(req)
    connexion.commit()
    return

if __name__=="__main__":
    connexion = sqlite3.connect('civilopedia.sqlite')
    cursor = connexion.cursor()
    req : str = f"SELECT Url_en FROM Urls WHERE Type='WON'"
    cursor.execute(req)
    connexion.commit()
    result = cursor.fetchall()
    for element in result:
        print(f"  {element}")
