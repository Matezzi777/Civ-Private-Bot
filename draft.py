#============================================= INITIALISATION ===============================================
#Import des modules
import discord
from discord.ext import commands
from random import *
import sqlite3
from classes import BotEmbed, SuccessEmbed, ErrorEmbed

#========================================= FONCTIONS PRINCIPALES ============================================
#génère une draft
async def make_draft(ctx : commands.Context, nb_civs : int) -> None:
    author = ctx.message.author
    if (not author.voice):
        embed=BotEmbed(title="🎤 JOIN A VOICE CHANNEL 🎤", description="Please, join a voice channel with the other players to use this command.\nIf you can't use the voice chat, consider using *$generic_draft* instead.")
        await ctx.send(embed=embed)
        return
    else:
        channel = author.voice.channel
        users = channel.members

    nb_users = len(users)
    if (nb_users < 2):
        embed = ErrorEmbed(description="It looks like you are alone here, find peoples to play with before to use this command.")
        await ctx.send(embed=embed)
        return
    elif (nb_users > 25):
        embed = ErrorEmbed(description="Too many players to start a draft (max. 25 players).")
        await ctx.send(embed=embed)
        return
    elif (nb_users * nb_civs > 77):
        embed = ErrorEmbed(title="PROCESS ABORTED", description="Too much leader by player. Retry with less civs by player.")
        await ctx.send(embed=embed)
        return
    elif (nb_civs > 15):
        embed = ErrorEmbed(title="PROCESS ABORTED", description="Maximum 15 civilizations by player.")
        await ctx.send(embed=embed)
        return
    else:
        message = ""
        i : int = 0
        while (i < len(users)):
            message = message + f"{users[i].mention} "
            i = i + 1
        await ctx.send(message)

        draft = create_draft(nb_users, nb_civs)
        embed=BotEmbed(title="DRAFT", description=f"New draft for {nb_users} players with {nb_civs} civilizations by player.")
        i : int = 0
        while(i < nb_users):
            k : int = 0
            message = f"**{users[i].mention} :**\n"
            while (k < nb_civs):
                message = message + f"{emote_from_id(draft[i*nb_civs+k])} {leader_from_id(draft[i*nb_civs+k])}\n"
                k = k + 1
            message = message[:-1]
            embed.add_field(name=f"", value=message, inline=True)
            i = i + 1
        await ctx.send(embed=embed)
        return
#génère une draft à l'aveugle
async def make_blind_draft(ctx : commands.Context, nb_civs : int) -> None:
    author = ctx.message.author
    if (not author.voice):
        embed=BotEmbed(title="🎤 JOIN A VOICE CHANNEL 🎤", description="Please, join a voice channel with the other players to use this command.\nIf you can't use the voice chat, consider using *$generic_draft* instead.")
        await ctx.send(embed=embed)
        return
    else:
        channel = author.voice.channel
        users = channel.members

    nb_users = len(users)
    if (nb_users < 2):
        embed = ErrorEmbed(description="It looks like you are alone here, find peoples to play with before to use this command.")
        await ctx.send(embed=embed)
    elif (nb_users > 25):
        embed = ErrorEmbed(description="Too many players to start a draft (max. 25 players).")
        await ctx.send(embed=embed)
        return
    elif (nb_users * nb_civs > 77):
        embed = ErrorEmbed(description="Too much leader by player. Use less civs/player or ban an innocent player 😈")
        await ctx.send(embed=embed)
        return
    elif (nb_civs > 15):
        embed = ErrorEmbed(description="Maximum 15 civilizations by player.")
        await ctx.send(embed=embed)
        return
    else:
        draft = create_draft(nb_users, nb_civs)
        i : int = 0
        while (i < nb_users):
            actual_user : discord.User = users[i]
            embed = BotEmbed(title="BLIND DRAFT", description="Here is your secret draft 🤫")
            message : str = ""
            j : int = 0
            while (j < nb_civs):
                message = message + f"{emote_from_id(draft[i*nb_civs+j])} {leader_from_id(draft[i*nb_civs+j])}\n"
                j = j + 1
            message = message[:-1]
            embed.add_field(name="", value=message)
            await send_embed_dm(actual_user, embed)
            i = i + 1
        embed_confirmation = SuccessEmbed(title="DRAFTS SENT", description="Check your private messages !")
        await ctx.send(embed=embed_confirmation)
        return
#génère une draft générique
async def make_generic_draft(ctx : commands.Context, players : int, nb_civs : int) -> None:
    if (players < 2):
        embed = ErrorEmbed(title="PROCESS ABORTED", description="Not enough players to start a draft (min. 2 players).")
        await ctx.send(embed=embed)
        return
    if (players > 25):
        embed = ErrorEmbed(title="PROCESS ABORTED", description="Too many players to start a draft (max. 25 players).")
        await ctx.send(embed=embed)
        return
    if (players * nb_civs > 77):
        embed = ErrorEmbed(title="PROCESS ABORTED", description="Too much leader by player. Use less civs/player or ban an innocent player 😈")
        await ctx.send(embed=embed)
        return
    if (nb_civs > 15):
        embed = ErrorEmbed(title="PROCESS ABORTED", description="Maximum 15 civilizations by player.")
        await ctx.send(embed=embed)
        return
    else :
        embed = BotEmbed(title="DRAFT", description=f"New draft for {players} players with {nb_civs} civilizations by player.")
        draft = create_draft(players, nb_civs)
        i : int = 0
        while(i < players):
            k : int = 0
            message = ""
            while (k < nb_civs):
                message = message + f"{emote_from_id(draft[i*nb_civs+k])} {leader_from_id(draft[i*nb_civs+k])}\n"
                k = k + 1
            message = message[:-1]
            embed.add_field(name=f"**Player {i+1}**", value=message, inline=True)
            i = i + 1
        await ctx.send(embed=embed)
        return

#Distribue les civilizations
def create_draft(players : int, nb_civs : int) -> list:
    i = 0
    draft = []
    
    while (i < players):
        j = 0
        while (j < nb_civs):
            id = 0
            while (id == 0 or is_n_in_list(id, draft)):
                id : int = randint(1, 77)
            draft.append(id)
            j = j + 1
        i = i + 1
    return (draft)

#========================================= FONCTIONS SECONDAIRES ============================================
#Envoie un message en privé à un joueur
async def send_dm(user : discord.User, content : str) -> None:
    await user.send(content=content)
    return
#Envoie un embed en privé à un joueur
async def send_embed_dm(user : discord.User, embed : BotEmbed) -> None:
    await user.send(embed=embed)
    return

#Récupère l'émote associée à l'id d'un leader
def emote_from_id(id : int) -> str:
    connexion = sqlite3.connect('db_leaders.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT Emoji FROM Leaders WHERE ID="+str(id)
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    return (trim(str(result)))
#Récupère le nom associé à l'id d'un leader
def leader_from_id(id : int) -> str:
    connexion = sqlite3.connect('db_leaders.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT Name FROM Leaders WHERE ID="+str(id)
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    return (trim(str(result)))
#Formate le résultat de la requète SQL
def trim(s : str) -> str:
    result = ""
    i = 0
    while (i < len(s)):
        if (not (s[i] == "(" or s[i] == "'" or s[i] == "," or s[i] == ")")):
            result = result + s[i]
        i = i + 1
    return (result)

#=============================================== BOOLÉENS ===================================================
#Vérifie la présence d'un élément dans la draft
def is_n_in_list(id : int, liste_totale : list) -> bool:
    i = 0
    while (i < len(liste_totale)):
        if (liste_totale[i] == id):
            return True
        i = i + 1
    return False
