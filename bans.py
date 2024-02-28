#============================================= INITIALISATION ===============================================
#Import des modules
import discord
from discord.ext import commands
from classes import BotEmbed, SuccessEmbed, ErrorEmbed, BansEmbed, ValidButton, Bans

#================================================ BOUTONS ===================================================

#================================================= VIEWS ====================================================

#=============================================== FONCTIONS ==================================================

async def make_bans(ctx : commands.Context) -> list[str]:
    author = ctx.message.author
    if (author.voice):
        channel = author.voice.channel
        users = channel.members
        print("    Users in the game :")
        i : int = 0
        while (i < len(users)):
            print(f"        @{users[i].name}")
            i = i + 1

    else:
        users = []
        users.append(author)
        print("    Command used without Voice Channel.")

    embed = BansEmbed(users, users)
    await ctx.send(embed=embed, view=Bans(users))
    