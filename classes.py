#============================================= INITIALISATION ===============================================
#Import des modules
import discord
from discord.ext import commands, tasks
from datetime import datetime, date
import sqlite3

#================================================= TASKS ====================================================

# @tasks.loop(time=datetime.time(hour=0, minute=0))
# async def check_birthday():
#     #Parsing today's date to be understund by the database
#     day = date.today().day
#     if (day < 10):
#         parsed_day : str = f"0{day}"
#     else:
#         parsed_day : str = f"{day}"
#     month = date.today().month
#     if (month < 10):
#         parsed_month : str = f"0{month}"
#     else:
#         parsed_month : str = f"{month}"
#     parsed_date : str = f"{parsed_day}{parsed_month}"
#     #Check in the database if there is a birthday today
#     connexion = sqlite3.connect('db.sqlite')
#     cursor = connexion.cursor()
#     request : str = f"SELECT User_ID FROM Anniversaires WHERE Date='{parsed_date}'"
#     cursor.execute(request)
#     connexion.commit()
#     result = cursor.fetchall()
#     connexion.close()

#     #Result
#     if (result):
#         await 
#     else:
        
#     return

#================================================== BOT =====================================================
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=discord.Intents.all(), description="Civ Private Bot v2.1")

    async def setup_hook(self):
        # check_birthday().start()
        await self.tree.sync()
    
    async def on_ready(self):
        print(f"{self.user.id} successfully logged in as {self.user.name}.\nRock n'Roll !")

#================================================= EMBEDS ===================================================
class BotEmbed(discord.Embed):
    def __init__(self, *, colour=discord.Colour.purple(), color=discord.Colour.purple(), title=None, type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
            )
        self.set_footer(text="Civ Private Bot 2.0")

class SuccessEmbed(discord.Embed):
    def __init__(self, *, colour=discord.Colour.green(), color=discord.Colour.green(), title="SUCCESS", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
            )
        self.set_footer(text="Civ Private Bot 2.0")

class ErrorEmbed(discord.Embed):
    def __init__(self, *, colour=discord.Colour.red(), color=discord.Colour.red(), title="ERROR", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
            )
        self.set_footer(text="Civ Private Bot 2.0")

# BUTTONS
#Bouton choix validé générique
class ValidButton(discord.ui.Button):
    def __init__(self) -> None:
        super().__init__(
            label=" - ",
            style=discord.ButtonStyle.green
        )
    
    async def callback(self, interaction : discord.Interaction):
        await interaction.response.edit_message(view=self.view)