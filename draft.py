################################################## INITIALISATION ##################################################

#import des librairies
import discord
from discord.ext import commands
from discord.ui import Button
from random import *
import sqlite3
from classes import CivPrivateBotEmbed

button_yes = Button(label="Yes", style=discord.ButtonStyle.green)
button_no = Button(label="No", style=discord.ButtonStyle.red)

#génère et envoie une draft
async def launch_draft(ctx : commands.Context, players : int, nb_civs : int):
    if (players < 2):
        embed = CivPrivateBotEmbed(title="Process aborted.", description="Not enough players to start a draft (min. 2 players).", colour=discord.Colour.red())
        return await ctx.send(embed=embed)
    if (players > 25):
        embed = CivPrivateBotEmbed(title="Process aborted.", description="Too many players to start a draft (max. 25 players).", colour=discord.Colour.red())
        return await ctx.send(embed=embed)
    if (players * nb_civs > 77):
        embed = CivPrivateBotEmbed(title="Process aborted.", description="Too much leader by player. Use less civs/player or ban an innocent player 😈", colour=discord.Colour.red())
        return await ctx.send(embed=embed)
    if (nb_civs > 15):
        embed = CivPrivateBotEmbed(title="Process aborted.", description="Maximum 15 civilizations by player.", colour=discord.Colour.red())
        return await ctx.send(embed=embed)
    else :
        embed = CivPrivateBotEmbed(title="DRAFT", description=f"New draft for {players} players with {nb_civs} civilizations by player.")
        draft = create_draft(players, nb_civs)
        i : int = 0
        while(i < players):
            k : int = 0
            message = ""
            while (k < nb_civs):
                message = message + f"{emote_from_id(draft[i*nb_civs+k])} {leader_from_id(draft[i*nb_civs+k])}\n"
                k = k + 1
            message = message[:-1]
            embed.add_field(name=f"Player {i+1}", value=message, inline=False)
            i = i + 1
        return await ctx.send(embed=embed)

#génère une draft
def create_draft(players : int, nb_civs : int):
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

#Vérifie la présence d'un élément dans la draft
def is_n_in_list(id : int, liste_totale : list):
    i = 0
    while (i < len(liste_totale)):
        if (liste_totale[i] == id):
            return (1)
        i = i + 1
    return (0)

#Récupère l'émote associée à l'id d'un leader
def emote_from_id(id : int):
    connexion = sqlite3.connect('db_leaders.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT Emoji FROM Leaders WHERE ID="+str(id)
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    return (trim(str(result)))

#Récupère le nom associé à l'id d'un leader
def leader_from_id(id : int):
    connexion = sqlite3.connect('db_leaders.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT Name FROM Leaders WHERE ID="+str(id)
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    return (trim(str(result)))

#Formate le résultat de la requète SQL
def trim(s : str):
    result = ""
    i = 0
    while (i < len(s)):
        if (not (s[i] == "(" or s[i] == "'" or s[i] == "," or s[i] == ")")):
            result = result + s[i]
        i = i + 1
    return (result)