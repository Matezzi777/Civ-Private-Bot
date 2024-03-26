#============================================= INITIALISATION ===============================================
#Import des modules
import discord
from discord.ext import commands
import sqlite3
from classes import BotEmbed, SuccessEmbed, ErrorEmbed

#=============================================== CONSTANTS ==================================================
months : list[str] = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#============================================ VIEWS & BUTTONS ===============================================
#View Birthdays
class BirthdayView(discord.ui.View):
    def __init__(self, caller : discord.User):
        super().__init__(timeout=None)
        self.add_item(PrevMonthButton())
        if (is_in_database(caller)):
            self.add_item(ChangeBirthdayButton())
        else:
            self.add_item(SetBirthdayButton())
        self.add_item(NextMonthButton())
#View Set Birthday
class SetBirthdayView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ConfirmButton())
        self.add_item(CancelButton())
#View Change Birthday
class ChangeBirthdayView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ConfirmButton())
        self.add_item(CancelButton())
        self.add_item(DeleteBirthdayButton())



#Button Previous Month
class PrevMonthButton(discord.ui.Button):
    def __init__(self, prev_month="Previous Month"):
        super().__init__(
            emoji="⬅",
            label=prev_month,
            style=discord.ButtonStyle.blurple,
            disabled=False
        )

    async def callback(self, interaction : discord.Interaction):
        return
#Button Next Month
class NextMonthButton(discord.ui.Button):
    def __init__(self, next_month="Next Month"):
        super().__init__(
            emoji="➡",
            label=next_month,
            style=discord.ButtonStyle.blurple,
            disabled=False
        )

    async def callback(self, interaction : discord.Interaction):
        return
#Button Set Birthday
class SetBirthdayButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Set Birthday",
            style=discord.ButtonStyle.grey,
            disabled=False
        )

    async def callback(self, interaction : discord.Interaction):
        return
#Button Change Birthday
class ChangeBirthdayButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Change birthday",
            style=discord.ButtonStyle.grey,
            disabled=False
        )

    async def callback(self, interaction : discord.Interaction):
        return
#Button Delete Birthday
class DeleteBirthdayButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Delete Actual Birthday",
            style=discord.ButtonStyle.grey,
            disabled=False
        )

    async def callback(self, interaction : discord.Interaction):
        return
#Button Confirm
class ConfirmButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            emoji="✅",
            style=discord.ButtonStyle.green,
            disabled=False
        )

    async def callback(self, interaction : discord.Interaction):
        return
#Button Cancel
class CancelButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            emoji="❌",
            style=discord.ButtonStyle.red,
            disabled=False
        )

    async def callback(self, interaction : discord.Interaction):
        return

#========================================= FONCTIONS PRINCIPALES ============================================

#$birthday
async def birthday_command(ctx : commands.Context) -> None:
    caller = ctx.message.author


#========================================= FONCTIONS SECONDAIRES ============================================

#=============================================== BOOLÉENS ===================================================

def is_in_database(user : discord.User) -> bool:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Date FROM Anniversaires WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    if (result):
        return (True)
    return (False)