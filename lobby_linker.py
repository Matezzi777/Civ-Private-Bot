import requests
import sqlite3
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from classes import SteamEmbed, BotEmbed, SuccessEmbed, ErrorEmbed, STEAM_RGB

#============ CONST =============

class LinkSteamModal(discord.ui.Modal):
    def __init__(self) -> None:
        super().__init__(title="Link your Steam account")
        self.add_item(discord.ui.InputText(style=discord.InputTextStyle.short, label="Enter you Steam profile URL :", placeholder="https://steamcommunity.com/id/Matezzi75/", min_length=30, max_length=60))

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        url : str = self.children[0].value
        if (check_correct_url(url)):
            html = get_html(url)
            name = get_steam_name_from_html(html)
            avatar_url = get_avatar_url_from_html(html)
            embed_response = BotEmbed(colour=STEAM_RGB, color=STEAM_RGB, title="CONFIRM ACCOUNT", description="Is that you ?")
            embed_response.set_thumbnail(url=avatar_url)
            embed_response.add_field(name=f"**Name :** {name}", value="")
            view_response = discord.ui.View()
            view_response.add_item(ConfirmAccountButton())
            view_response.add_item(CancelAccountButton())
            await interaction.response.edit_message(embed=embed_response, view=view_response)
        else:
            embed_response = ErrorEmbed()
            await interaction.response.edit_message(embed=embed_response)

class LinkSteamView(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
        self.add_item(StartLinkButton())

class StartLinkButton(discord.ui.Button):
    def __init__(self) -> None:
        super().__init__(label="🔗 Link your account", style=discord.ButtonStyle.green)
        self.disabled=False

    def callback(self, interaction: discord.Interaction):
        self.disabled=True
        return interaction.response.send_modal(LinkSteamModal())

class ConfirmAccountButton(discord.ui.Button):
    def __init__(self) -> None:
        super().__init__(label="✅ Confirm", style=discord.ButtonStyle.green)

    def callback(self, interaction: discord.Interaction):
        embed = SuccessEmbed(description="Your account is now linked, use the command again to display a link to your lobby")
        # store_account_in_database(user, url)
        return interaction.response.edit_message(embed=embed, view=None)

class CancelAccountButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="❌ Not me", style=discord.ButtonStyle.red)
    
    def callback(self, interaction : discord.Interaction):
        embed = ErrorEmbed(title="PROCESS CANCELED", description="Please make sure you used the good url, and use *$feedback* if it does not fix the problem.")
        return interaction.response.edit_message(embed=embed, view=None)
    
#============ FUNCT =============

#Ajoute l'url de l'utilisateur dans la base de données
async def link_steam_account(ctx : commands.Context):
    embed = SteamEmbed()
    view = LinkSteamView()
    await ctx.send(embed=embed, view=view)

#Affiche le lien du lobby à partir de l'url
# async def display_lobby_link(ctx : commands.Context, html):
#     ...

#Teste la validité du lien
def check_correct_url(url) -> bool:
    html = get_html(url)
    if (html):
        print(f"  HTML code loaded.")
        name = get_steam_name_from_html(html)
        if (name):
            print(f"  Name found : {name}")
            avatar_url = get_avatar_url_from_html(html)
            if (avatar_url):
                print(f"  Avatar URL found : {avatar_url}")
                return (1)
            else:
                print(f"  ERROR : Unable to get the Avatar URL from this HTML")
        else:
            print(f"  ERROR : Unable to get the Name from this HTML")
    else:
        print(f"  ERROR : Unable to get the HTML code of this url :\n    {url}")
        return (0)

#============ SUB-F =============

#Retourne la code HTML de l'url en paramètre
def get_html(url : str):
    response = requests.get(url)
    return (response.text)
#Retourne le nom du profil de l'url
def get_steam_name_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('span', class_='actual_persona_name').text
    return(name)
#Retourne l'url de la photo du profil de l'url
def get_avatar_url_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    is_border = soup.find('div', class_='profile_avatar_frame')
    if (is_border):
        avatar = is_border.find_next_sibling('img')
        avatar_url = avatar['src']
    else:
        avatar = soup.find('div', class_='playerAvatarAutoSizeInner').find('img')
        avatar_url = avatar['src']
    return (avatar_url)


#Enregistre le compte dans la base de donnée
def store_account_in_database(user : discord.User, url : str):
    ...