#============================================= INITIALISATION ===============================================
#Import des modules
import requests
import urllib.request
import sqlite3
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from classes import BotEmbed, SuccessEmbed, ErrorEmbed