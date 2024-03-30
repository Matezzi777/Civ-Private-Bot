#============================================= INITIALISATION ===============================================
#Import des modules
import discord
import discord.ext
import requests
from bs4 import BeautifulSoup
from classes import Bot, BotEmbed, SuccessEmbed, ErrorEmbed

url = 'https://www.civilopedia.net/fr/gathering-storm/civilizations/civilization_france'

requests.get(url)

