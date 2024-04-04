import requests
import sqlite3
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from classes import SteamEmbed, BotEmbed, STEAM_RGB

#============ CONST =============

class LinkSteamModal(discord.ui.Modal):
    def __init__(self) -> None:
        super().__init__(title="Link your Steam account")
        self.add_item(discord.ui.InputText(style=discord.InputTextStyle.short, label="Enter you Steam profile URL :", placeholder="https://steamcommunity.com/id/Matezzi75/", min_length=30, max_length=60))

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        url : str = self.children[0].value
        embed = BotEmbed(colour=STEAM_RGB, color=STEAM_RGB, title="PROCESSING...")
        if (check_correct_url(url)):
            await interaction.response.send_message(embed=embed, ephemeral=True)

class LinkSteamView(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
        self.add_item(StartLinkButton())

class StartLinkButton(discord.ui.Button):
    def __init__(self) -> None:
        super().__init__(label="Link your account 🔗", style=discord.ButtonStyle.green)
    
    def callback(self, interaction: discord.Interaction):
        return interaction.response.send_modal(LinkSteamModal())

#============ FUNCT =============

#Ajoute l'url de l'utilisateur dans la base de données
async def link_steam_account(ctx : commands.Context):
    embed = SteamEmbed()
    # view = 

#Affiche le lien du lobby à partir de l'url
async def display_lobby_link(ctx : commands.Context, html):
    ...

#Teste la validité du lien
def check_correct_url(url) -> int:
    ...

#============ SUB-F =============

