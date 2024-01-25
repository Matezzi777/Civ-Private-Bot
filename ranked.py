##################################################     INITIALISATION    ##################################################

import discord
from discord.ext import commands
import sqlite3
import datetime
from classes import CivPrivateBotEmbed



##################################################       COMMANDES       ##################################################

#Affiche les statistiques de l'utilisateur 
async def show_stats(ctx : commands.Context, user : discord.User):
    if (is_user_in_database(user)):
        elo = get_elo(user)
        wins = get_wins(user)
        top1 = get_top1(user)
        lost = get_lost(user)
        date = parse_date_ranked(get_date_from_database(user))
        embed = CivPrivateBotEmbed(title="STATS", description=f"## **{user.global_name.capitalize()}**\nDiscord Name : {user.name}\nGames played in Civ Private Club : {wins+lost}")
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name="1v1", value=f"📈 **ELO** : N/A\n🟢 **TOP 1** : N/A\n🟡 **WINS** : N/A\n🔴 **LOST** : N/A\n⏲ **LAST** : N/A", inline=False)
        embed.add_field(name="FFA", value=f"📈 **ELO** : {elo}\n🟢 **TOP 1** : {top1}\n🟡 **WINS** : {wins}\n🔴 **LOST** : {lost}\n⏲ **LAST** : {date}", inline=False)
        embed.add_field(name="Teamer", value=f"📈 **ELO** : N/A\n🟢 **TOP 1** : N/A\n🟡 **WINS** : N/A\n🔴 **LOST** : N/A\n⏲ **LAST** : N/A", inline=False)
        return await ctx.send(embed=embed)
    else:
        embed = CivPrivateBotEmbed(colour=discord.Colour.red(), title="Process aborted", description=f"No result for <@{user.id}> in the database.")
        return await ctx.send(embed=embed, delete_after=7)
#$Rapporte le résultat d'un match
async def build_message(ctx : commands.Context, players : int, liste_players : list):
    embed = discord.Embed(colour=discord.Colour.purple(), title="Verify the result", description="This message has to be ✅ by :\nBoth players in 1v1.\nMinimum 3 players in FFA.")
    message : str = f"1 : <@{liste_players[0].id}>"
    i : int = 1
    while (i < players):
        message = message + f"\n{i+1} : <@{liste_players[i].id}>"
        i = i + 1
    embed.add_field(name="Result reported", value=message)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("✅")
#$Affiche le classement du serveur
#$Calcule le nouvel elo des joueurs après le résultat d'un match
#$Met à jour la base de donnée avec les nouvelles données



##################################################       FONCTIONS       ##################################################

#Ajoute un nouvel utilisateur à la base de donnée
async def add_user(ctx : commands.Context, user : discord.User):
    if (not is_user_in_database(user)):
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request : str = "INSERT INTO Ranked VALUES ('"+str(user.id)+"', '1000','0','0','0','0')"
        print("New user added.")
        cursor.execute(request)
        connexion.commit()
        connexion.close()
        return await ctx.send("User added in the database.")
    else:
        return await ctx.send("User already in the database.")
#Supprime un utilisateur de la base de donnée
async def remove_user(ctx : commands.Context, user : discord.User):
    if (is_user_in_database(user)):
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request : str = "DELETE FROM Ranked WHERE User_ID='"+str(user.id)+"'"
        print("User removed.")
        cursor.execute(request)
        connexion.commit()
        connexion.close()
        return await ctx.send("User removed.")
    else:
        return await ctx.send("User not found in the database, nothing to delete")

#Met à jour les Wins de l'utilisateur
async def update_win(ctx : commands.Context, user : discord.User):
    if (is_user_in_database(user)):
        win : int = get_wins(user)
        new_win : int = win + 1
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request : str = "UPDATE Ranked SET Wins='"+str(new_win)+"' WHERE User_ID='"+str(user.id)+"'"
        cursor.execute(request)
        print("User's Wins updated.")
        connexion.commit()
        connexion.close
        return await ctx.send("Wins Updated.")
    else:
        return await ctx.send("User not found.")
#Met à jour les Top1 de l'utilisateur
async def update_top1(ctx : commands.Context, user : discord.User):
    if (is_user_in_database(user)):
        top1 : int = get_top1(user)
        new_top1 : int = top1 + 1
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request_write : str = "UPDATE Ranked SET Top1='"+str(new_top1)+"' WHERE User_ID='"+str(user.id)+"'"
        cursor.execute(request_write)
        print("User's Top1 updated.")
        connexion.commit()
        connexion.close
        return await ctx.send("Top 1 updated.")
    else:
        return await ctx.send("User not found.")
#Met à jour les Lost de l'utilisateur
async def update_lost(ctx : commands.Context, user : discord.User):
    if (is_user_in_database(user)):
        lost : int = get_lost(user)
        new_lost : int = lost + 1
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request_write : str = "UPDATE Ranked SET Lost='"+str(new_lost)+"' WHERE User_ID='"+str(user.id)+"'"
        cursor.execute(request_write)
        print("User's Lost updated.")
        connexion.commit()
        connexion.close
        return await ctx.send("User's Lost updated.")
    else:
        return await ctx.send("User not found.")
#Met à jour la Date de l'utilisateur
async def update_date(ctx : commands.Context, user : discord.User):
    if (is_user_in_database(user)):
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        date : str = get_date()
        request_write : str = "UPDATE Ranked SET Date='"+str(date)+"' WHERE User_ID='"+str(user.id)+"'"
        cursor.execute(request_write)
        print("User's Last Game Date updated.")
        connexion.commit()
        connexion.close
        return await ctx.send("User's Date updated.")
    else:
        return await ctx.send("User not found.")
#Met à jour l'Elo de l'utilisateur
async def update_elo(ctx : commands.Context, user : discord.User, elo : int):
    if (is_user_in_database(user)):
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request_write : str = "UPDATE Ranked SET Elo='"+str(elo)+"' WHERE User_ID='"+str(user.id)+"'"
        cursor.execute(request_write)
        print("User's Elo updated.")
        connexion.commit()
        connexion.close
        return await ctx.send("User's Elo updated.")
    else:
        return await ctx.send("User not found.")

#Récupère les Wins d'un utilisateur
def get_wins(user : discord.User):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request_get : str = "SELECT Wins FROM Ranked WHERE User_ID='"+str(user.id)+"'"
    cursor.execute(request_get)
    connexion.commit()
    win : int = int(cursor.fetchone()[0])
    return (win)
#Récupère les Top1 d'un utilisateur
def get_top1(user : discord.User):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request_get : str = "SELECT Top1 FROM Ranked WHERE User_ID='"+str(user.id)+"'"
    cursor.execute(request_get)
    connexion.commit()
    top1 : int = int(cursor.fetchone()[0])
    return (top1)
#Récupère les Lost d'un utilisateur
def get_lost(user : discord.User):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request_get : str = "SELECT Lost FROM Ranked WHERE User_ID='"+str(user.id)+"'"
    cursor.execute(request_get)
    connexion.commit()
    lost : int = int(cursor.fetchone()[0])
    return (lost)
#Récupère la date actuelle et la formate pour être stockée dans la base de donnée
def get_date():
    datenow : str = str(datetime.date.today())
    date : str = datenow[8] + datenow[9] + datenow[5] + datenow[6] + datenow[0] + datenow[1] + datenow[2] + datenow[3]
    return (date)
#Récupère l'elo d'un utilisateur
def get_elo(user : discord.User):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request_get = "SELECT Elo FROM Ranked WHERE User_ID='"+str(user.id)+"'"
    cursor.execute(request_get)
    connexion.commit()
    elo : int = int(cursor.fetchone()[0])
    return (elo)
#Récupère la date de la dernière partie du joueur enregistrée
def get_date_from_database(user : discord.User):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request_get = "SELECT Date FROM Ranked WHERE User_ID='"+str(user.id)+"'"
    cursor.execute(request_get)
    connexion.commit()
    date : int = int(cursor.fetchone()[0])
    return (date)

#Formate la date pour être affichée
def parse_date_ranked(date : str):
    if (int(date) == 0):
        date_parsed : str = "00/00/0000"
    else:
        date_parsed : str = str(date)[0]+str(date)[1]+"/"+str(date)[2]+str(date)[3]+"/"+str(date)[4]+str(date)[5]+str(date)[6]+str(date)[7]
    return (date_parsed)



################################## BOOLEENS ##################################

#Check si l'utilisateur est dans la base de donnée
def is_user_in_database(user : discord.User):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT User_ID FROM Ranked WHERE User_ID='"+str(user.id)+"'"
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    if (result):
        return True
    else:
        return False
