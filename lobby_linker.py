import requests
import sqlite3
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from classes import SteamEmbed, BotEmbed, SuccessEmbed, ErrorEmbed

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
            embed_response = SteamEmbed(title="CONFIRM ACCOUNT", description="Is that you ?")
            embed_response.set_thumbnail(url=avatar_url)
            embed_response.add_field(name=f"**Name :** {name}", value="")
            view_response = discord.ui.View()
            view_response.add_item(ConfirmAccountButton(user, url))
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
        super().__init__(label="🔗 Link my profile", style=discord.ButtonStyle.green)
        self.disabled=False

    def callback(self, interaction: discord.Interaction):
        self.disabled=True
        print(f"  Modal sent")
        return interaction.response.send_modal(LinkSteamModal())
class ConfirmAccountButton(discord.ui.Button):
    def __init__(self, user, account_url) -> None:
        super().__init__(label="✅ Confirm", style=discord.ButtonStyle.green)
        self.user_to_remember = user
        self.account_url = account_url

    def callback(self, interaction: discord.Interaction):
        embed = SuccessEmbed(description="Your account is linked!\n\nYou can now use *$lobby* to create a link to your lobby.")
        store_account_in_database(self.user_to_remember, self.account_url)
        self.disabled=True
        return interaction.response.edit_message(embed=embed, view=None)
class CancelAccountButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="❌ Not me", style=discord.ButtonStyle.red)
    
    def callback(self, interaction : discord.Interaction):
        embed = ErrorEmbed(title="PROCESS CANCELED", description="Please make sure you used the good url, and use *$feedback* if it does not fix the problem.")
        self.disabled=True
        return interaction.response.edit_message(embed=embed, view=None)

class AllGoodButton(discord.ui.Button):
    def __init__(self, involved_user) -> None:
        super().__init__(
            label="✅ Confirm the account",
            style=discord.ButtonStyle.green)
        self.involved_user = involved_user

    def callback(self, interaction: discord.Interaction):
        user : discord.User = interaction.user
        if (user==self.involved_user):
            embed=SuccessEmbed(title="ACCOUNT CONFIRMED", description="Your account is still linked and stored in the database.")
            self.disabled=True
            return interaction.response.edit_message(embed=embed, view=None)
        else:
            embed = ErrorEmbed(title="THIS DOESN'T CONCERN YOU", description="You tried to click on a button which does not concern you.\n\nIf you want to delete your Steam profile from the database, use *$set_steam* by yourself.")
            self.disabled=True
            return interaction.response.send_message(embed=embed, ephemeral=True)
class ChangeButton(discord.ui.Button):
    def __init__(self, involved_user) -> None:
        super().__init__(
            label="♻ Change linked account",
            style=discord.ButtonStyle.blurple)
        self.involved_user = involved_user

    def callback(self, interaction: discord.Interaction):
        user : discord.User = interaction.user
        if (user == self.involved_user):
            self.disabled=True
            return interaction.response.send_modal(LinkSteamModal())
        else:
            embed = ErrorEmbed(title="THIS DOESN'T CONCERN YOU", description="You tried to click on a button which does not concern you.\n\nIf you want to delete your Steam profile from the database, use *$set_steam* by yourself.")
            self.disabled=True
            return interaction.response.send_message(embed=embed, ephemeral=True)
class DeleteButton(discord.ui.Button):
    def __init__(self, user_involved : discord.User) -> None:
        super().__init__(
            label="❌ Delete linked account",
            style=discord.ButtonStyle.red)
        self.user_involved = user_involved

    def callback(self, interaction: discord.Interaction):
        if (interaction.user == self.user_involved):
            remove_user(interaction.user)
            embed = ErrorEmbed(title="ACCOUNT DELETED", description="Your account has been deleted from the database.")
            self.disabled=True
            return interaction.response.send_message(embed=embed)
        else:
            embed = ErrorEmbed(title="THIS DOESN'T CONCERN YOU", description="You tried to click on a button which does not concern you.\n\nIf you want to delete your Steam profile from the database, use *$set_steam* by yourself.")
            self.disabled=True
            return interaction.response.send_message(embed=embed, ephemeral=True)



#============ FUNCT =============

#Ajoute l'url de l'utilisateur dans la base de données
async def link_steam_account(ctx : commands.Context):
    user = ctx.message.author
    if (is_user_in_db(user)):
        loading_embed = SteamEmbed(title="LOADING", description=None)
        await ctx.send(embed=loading_embed)
        embed = SteamEmbed(title="ACCOUNT LINKED", description="Your account is already linked.")
        url = get_user_url_from_db(user)
        html = get_html(url)
        profile_name = get_steam_name_from_html(html)
        avatar_url = get_avatar_url_from_html(html)
        embed.set_thumbnail(url=avatar_url)
        embed.add_field(name=f"**Name** : {profile_name}", value=f"", inline=False)
        embed.add_field(name="**Do you want to change it ?**", value=f"", inline=False)
        view = discord.ui.View()
        view.add_item(AllGoodButton(user))
        view.add_item(ChangeButton(user))
        view.add_item(DeleteButton(user))

        async for message in ctx.channel.history(limit=1):
            await message.delete()
        await ctx.send(embed=embed, view=view)

    else:
        embed = SteamEmbed()
        view = LinkSteamView()
        await ctx.send(embed=embed, view=view)

#Affiche le lien du lobby à partir de l'url
async def display_lobby_link(ctx : commands.Context):
    user = ctx.message.author
    if (is_user_in_db(user)):
        steam_profile_url = get_user_url_from_db(user)
        html = get_html(steam_profile_url)
        avatar_url = get_avatar_url_from_html(html)
        lobby_long_link = get_lobby_link_from_html(html)
        if (lobby_long_link):
            short_url = shorten_url(lobby_long_link)
            if (short_url):
                embed = SteamEmbed(title=f"JOIN LOBBY", description=None)
                embed.set_thumbnail(url=avatar_url)
                embed.add_field(name="", value=f"**{user.mention} is hosting** :\n    [JOIN THE LOBBY]({short_url})")
                print(f"  Lobby link created and sent in #{ctx.message.channel}")
                await ctx.send(embed=embed, view=None)
            else:
                embed = ErrorEmbed(title="UNABLE TO SHORTEN THIS LINK", description="Oops..! An error happened while shortening the url...")
                print(f"  Unable to shorten this link")
                await ctx.send(embed=embed)
        else:
            embed = SteamEmbed(title="UNABLE TO FIND THE LOBBY", description="Make sure your Profile is public and you have a lobby open.\n\nIf this don't fix the problem, use *$feedback* to open a ticket.")
            print(f"  Unable to find the lobby link")
            await ctx.send(embed=embed)
    else:
        embed = SteamEmbed(title="LINK YOU STEAM PROFILE FIRST", description="You don't have linked your steam profile yet !\n\nTo be able to use *$lobby*, you have to link your steam account first.")
        embed.add_field(name="**How to link my steam profile ?**", value="Click the button **🔗 Link my profile** or use the command *$set_steam* to llink your profile.")
        view = LinkSteamView()
        await ctx.send(embed=embed, view=view)



#============ SUB-F =============

#Retourne la code HTML de l'url en paramètre
def get_html(url : str):
    response = requests.get(url)
    return (response.text)
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
#Récupère l'url du profile de l'utilisateur depuis la base de donnée
def get_user_url_from_db(user : discord.User) -> str:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Profile_url FROM Steam WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    url = cursor.fetchone()
    return (url[0])
#Récupère le lien du lobby
def get_lobby_link_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    lobby_link = soup.find('a', class_='btn_green_white_innerfade')
    if (lobby_link):
        lobby_url = lobby_link['href']
    else:
        lobby_url = None
    return (lobby_url)

#Supprime l'utilisateur de la base de donnée
def remove_user(user : discord.User):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request = f"DELETE FROM Steam WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    print(f"  @{user.name}'s steam profile erased from the database")
#Enregistre le compte dans la base de donnée
def store_account_in_database(user : discord.User, url : str):
    html = get_html(url)
    profile_name = get_steam_name_from_html(html)
    avatar_url = get_avatar_url_from_html(html)

    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    if (is_user_in_db(user)):
        request : str = f"UPDATE Steam SET Profile_name='{profile_name}', Profile_url='{url}', Avatar_url='{avatar_url}' WHERE User_ID='{user.id}'"
        print(f"  Users infos updated")
    else:
        request : str = f"INSERT INTO Steam VALUES ('{user.id}', '{profile_name}','{url}','{avatar_url}')"
        print(f"  @{user.name}'s steam profile added to the database")
    cursor.execute(request)
    connexion.commit()
    connexion.close()
#Vérifie la présence d'un utilisateur dans la base de données
def is_user_in_db(user : discord.User) -> bool:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT * FROM Steam WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    if (result):
        return True
    return False

def shorten_url(long_url):
    base_url = "http://tinyurl.com/api-create.php?url="
    response = requests.get(f"{base_url}{long_url}")
    short_url = response.text
    return (short_url)