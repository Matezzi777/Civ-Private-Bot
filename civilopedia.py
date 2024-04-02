#============================================= INITIALISATION ===============================================
#Import des modules
import requests
import sqlite3
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from classes import BotEmbed, SuccessEmbed, ErrorEmbed

#============================================== CONSTANTES ==================================================

URL_BASE = "https://www.civilopedia.net"

#================================================ CLASSES ===================================================


#=============================================== FONCTIONS ==================================================
#Lance la commande $civilopedia
async def make_civilopedia(ctx : commands.Context, article : str = None, lang : str = "en"):
    if (article == None): #Si aucun article n'est renseigné
        embed = SuccessEmbed(title="BROWSER", description="No specific article mentionned.\n\nThe browser will be displayed here later...")
        await ctx.send(embed=embed)

    else: #Si un article est renseigné
        if (check_article_in_db(article)): #Si l'article est trouvé dans la base de donnée
            if (is_valid_lang(lang)): #Si la langue est valide
                url = find_url(article, lang)
                await display_article(ctx, article, url)

            else: #Si la langue n'est pas valide
                embed = ErrorEmbed(title="LANGUAGE NOT SUPPORTED", description=f"Language '*{lang}*' not supported.\n\nPlease use one of the following languages :\n\n- **en** : 🇺🇸\n- **de** : 🇩🇪\n- **es** : 🇪🇸\n- **fr** : 🇫🇷\n- **it** : 🇮🇹\n- **pl** : 🇵🇱\n- **pt** : 🇵🇹\n- **ru** : 🇷🇺")
                await ctx.send(embed=embed)

        else: #Si l'article n'est pas trouvé dans la base de donnée
            embed = ErrorEmbed(title="ARTICLE NOT FOUND", description=f"No article found for : '*{article}*'.")
            await ctx.send(embed=embed)
#Affiche l'article demandé
async def display_article(ctx : commands.Context, article : str, url : str):
    type_article : str = find_type(article)

    if (not type_article): #Si erreur lors de la récupération du type
        print("  Error while getting the type of the article.")
        embed = ErrorEmbed(title="ERROR", description="Error while getting the type of the article.")
        await ctx.send(embed=embed)

    else : #Si le type de page est supporté (CIV/LEA/DIS/CS)
        html = get_html(url)

        #1. Récupérer le titre à partir de l'url
        print(f"  Extracting {article}'s title...")
        article_title : str = extract_title_from_html(html)
        print(f"    {article}'s title found : {article_title}")

        #2. Récupérer l'image à partir de l'url
        print(f"  Extracting {article}'s icon...")
        url_image : str = extract_image_from_html(html, type_article)
        print(f"    {article}'s icon url found : {url_image}")

        #3. Récupérer les titres des fields à partir de l'url
        print(f"  Extracting embed's fields titles...")
        sections_titles : list[str] = extract_sections_titles_from_html(html, type_article)
        log : str = f"    Fields titles found : "
        for field in sections_titles:
            log = log + f"'{field}' "
        print(f"{log}")

        #4. Récupérer les contenus des fields à partir de l'url
        print(f"  Extracting embed's fields contents...")
        sections_contents : list[str] = extract_sections_contents_from_html(html, type_article)
        print(f"    Fields content found : {len(sections_contents)}")

        #5. Construction de l'embed
        embed = BotEmbed(title=article_title.upper(), description=f"[Link to civilopedia.net]({url})")
        nb_sections : int = len(sections_titles)
        i : int = 0
        while (i < nb_sections):
            embed.add_field(name=sections_titles[i], value=sections_contents[i], inline=False)
            i = i + 1

        embed.set_thumbnail(url=f"{url_image}")
        #7. Envoi de l'embed
        await ctx.send(embed=embed)
        print(f"  Article {article_title} displayed in {ctx.message.channel}")

#============================================= SUB-FONCTIONS ================================================
#Retrouve l'url d'un article à partir de son nom
def find_url(article : str, lang : str = "en") -> str:
    print(f"  Finding {article}'s url...")
    connexion = sqlite3.connect('civilopedia.sqlite')
    cursor = connexion.cursor()
    req_read_articles : str = f"SELECT Url_{lang} FROM Urls WHERE Name='{article}'"
    cursor.execute(req_read_articles)
    connexion.commit()
    result : str = cursor.fetchone()[0]
    connexion.close()
    if (not result):
        print(f"    {article}'s url not found.")
        return (None)
    else:
        print(f"    {article}'s url found : {result}")
        return (result)
#Retrouve le type de l'article à partir de son nom
def find_type(article : str) -> str:
    print(f"  Finding {article}'s type...")
    connexion = sqlite3.connect('civilopedia.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Type FROM Urls WHERE Name='{article}'"
    cursor.execute(request)
    connexion.commit()
    result : str = cursor.fetchone()[0]
    connexion.close()
    if (not result):
        print(f"    {article}'s type not found.")
        return (None)
    else:
        print(f"    {article}'s type found : {result}")
        return (result)

#Vérifie si la langue entrée est prise en charge
def is_valid_lang(lang : str) -> bool:
    if (lang in ["en", "de", "es", "fr", "it", "it", "pl", "pt", "ru"]):
        return (True)
    return (False)
#Vérifie la présence de l'article dans la base de données
def check_article_in_db(article : str) -> bool:
    print("  Checking database...")
    connexion = sqlite3.connect('civilopedia.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Name FROM Urls WHERE Name='{article}'"
    cursor.execute(request)
    connexion.commit()
    result : str = cursor.fetchone()
    connexion.close()
    if (not result):
        print(f"    {article} not stored in the database.")
        return (False)
    else:
        print(f"    {article} stored in database.")
        return (True)



#========================================== FONCTIONS SCRAPING ==============================================

#Retourne la code HTML de l'url en paramètre
def get_html(url : str):
    response = requests.get(url)
    return (response.text)

#Extrait le title de l'article à partir de son code HTML
def extract_title_from_html(html : str):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('div', class_='App_pageHeaderText__SsfWm')
    return (title.text)
#Extrait l'url de l'image de l'article à partir de son code HTML
def extract_image_from_html(html : str, type_article : str):
    soup = BeautifulSoup(html, 'html.parser')
    if (type_article == "CIV" or type_article=="DIS" or type_article=="CS"): #Si type CIV DIS ou CS
        images = soup.find('div', class_='Component_portraitContent__TiPGl').find_all('img')
        for image in images:
            if (image['src'][0] == '/'):
                url : str = f"{URL_BASE}{image['src']}"
                return (url)
    elif (type_article == "LEA"): #Si type LEA
        images = soup.find('div', class_='Component_portraitTall___EClU').find_all('img')
        for image in images:
            if (image['src'][0] == '/'):
                url : str = f"{URL_BASE}{image['src']}"
                return (url)
    else:
        print(f"    Unable to find icon of {type_article} type.")
        return None
#Extrait le titre des fields de l'embed
def extract_sections_titles_from_html(html : str, type_article : str) -> list[str]:
    sections_titles : list[str] = []
    soup = BeautifulSoup(html, 'html.parser')
    if (type_article == "CIV"):
        sections_titles.append("**Leaders :**")
        ability_title : str = "**Ability :** "
        ability_name = soup.find('p', class_='Component_headerBodyHeaderText__LuO9w').text
        ability_title = ability_title+ability_name
        sections_titles.append(ability_title)
        sections_titles.append("**UU :**")
        sections_titles.append("**UI :**")

    elif (type_article == "LEA"):
        sections_titles.append("**Civilizations :**")
        ability_title : str = "**Ability :** "
        ability_name = soup.find('p', class_='Component_headerBodyHeaderText__LuO9w').text
        ability_title = ability_title+ability_name
        sections_titles.append(ability_title)
        sections_titles.append("**Description :**")
        sections_titles.append("**AI Agenda :**")
        sections_titles.append("**AI Religion :**")

    elif (type_article == "DIS"):
        sections_titles.append("**Description :**")
        stat_box_headers = soup.find_all('div', class_='StatBox_statBoxHeaderText__bedSz')
        nb_fields : int = len(stat_box_headers) / 2
        i : int = 0
        while (i < nb_fields):
            sections_titles.append(stat_box_headers[i].text)
            i = i + 1

    
    elif (type_article == "CS"):
        details_titles = soup.find_all('p', class_='Component_headerBodyHeaderText__LuO9w')
        nb_fields : int = len(details_titles) / 2
        i : int = 0
        while (i < nb_fields):
            sections_titles.append(details_titles[i].text)
            i = i + 1

    else:
        print(f"    Unable to find sections titles of {type_article} type.")
        return None
    
    return (sections_titles)
#Extrait le contenu des fields de l'embed
def extract_sections_contents_from_html(html, type_article) -> list[str]:
    sections_contents : list[str] = []
    soup = BeautifulSoup(html, 'html.parser')
    if (type_article == "CIV"):
        
        ...

    elif (type_article == "LEA"):
        ...

    elif (type_article == "DIS"):
        ...

    elif (type_article == "CS"):
        details_content = soup.find_all('p', class_='Component_headerBodyHeaderBody__MkvCp')
        nb_fields : int = len(details_content) / 2
        i : int = 0
        while (i < nb_fields):
            sections_contents.append(parse_field_content(details_content[i].text))
            i = i + 1

    else:
        print(f"    Unable to find sections content of {type_article} type.")
        return None

    return (sections_contents)

#Met en forme le contenu des fields (remplace les '.' par '.\n')
def parse_field_content(content : str) -> str:
    parsed_content : str = ""
    len_content : int = len(content)
    i : int = 0
    while (i < len_content):
        if (content[i] == '.'):
            parsed_content = parsed_content + ".\n"
        else:
            parsed_content = parsed_content + content[i]
        i = i + 1
    return (parsed_content)

