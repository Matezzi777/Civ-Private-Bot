#============================================= INITIALISATION ===============================================
#Import des modules
import requests
import sqlite3
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from classes import BotEmbed, SuccessEmbed, ErrorEmbed

#================================================ CLASSES ===================================================

class ArticleEmbed(discord.Embed):
    def __init__(self, *, title="TITLE", url=None, infos=None, effects=None, timestamp=None) -> None:
        super().__init__(
            colour=discord.Colour.purple(),
            title=title,
            type='rich',
            url=url,
            description="",
            timestamp=timestamp
            )
        self.set_thumbnail(url)
        if (infos):
            self.add_field(name="INFOS :", value=infos)
        if (effects):
            self.add_field(name="EFFECTS :", value=effects)

#=============================================== FONCTIONS ==================================================

#Ouvre le navigateur de la civilopedia
async def navigate_civilopedia(ctx : commands.Context, ) -> None:
    ...

#============================================= SUB-FONCTIONS ================================================
    