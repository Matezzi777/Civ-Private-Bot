#============================================= INITIALISATION ===============================================
#Import des modules
import discord
from discord.ext import commands
import sqlite3
import datetime
from classes import CivPrivateBotEmbed

#========================================= FONCTIONS PRINCIPALES ============================================
#Ajoute un anniversaire dans la base de donnée
def add_birthday(user : discord.User, date : int) -> None:
    if (check_birthday(user)):
        print("Birthday already in Database")
    else:
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request : str = "INSERT INTO Anniversaires (User_ID, Date) VALUES ("+str(user.id)+", "+str(date)+")"
        cursor.execute(request)
        connexion.commit()
        connexion.close()
    return
#Supprime un anniversaire de la base de donnée
def rem_birthday(user : discord.User) -> None:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "DELETE FROM Anniversaires WHERE User_id='"+str(user.id)+"'"
    cursor.execute(request)
    connexion.commit()
    connexion.close()
    return
#Affiche les anniversaire stockés dans la base de donnée
async def display_birthdays(ctx : commands.Context) -> None:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT User_ID, Date FROM Anniversaires"
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchall()
    connexion.close()
    if(result):
        embed=CivPrivateBotEmbed(title="BIRTHDAYS", description="Birthdays stored in the database :")
        for row in result:
            user = ctx.guild.get_member(row[0])
            embed.add_field(name="", value=f"<@{user.id}> : {parse_date(row[1])}", inline=False)
        await ctx.send(embed=embed)
    else:
        embed=CivPrivateBotEmbed(title="Process aborted", description="No birthday stored in the database.")
        await ctx.send(embed=embed)
    return
#Affiche la date (format : DD/MM/YYYY)
async def display_date(ctx : commands.Context) -> None:
    day = str(datetime.date.today())[8] + str(datetime.date.today())[9]
    month = str(datetime.date.today())[5] + str(datetime.date.today())[6]
    year = str(datetime.date.today())[0] + str(datetime.date.today())[1] + str(datetime.date.today())[2] + str(datetime.date.today())[3]
    embed = CivPrivateBotEmbed(title="DATE", description=f"Today is : **{day}/{month}/{year}** (UTC + 1)")
    await ctx.send(embed=embed)
    return

#========================================= FONCTIONS SECONDAIRES ============================================
#Modifie la date d'anniversaire de l'utilisateur 
def change_birthday(user : discord.User, date : str) -> None:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    cursor.execute("UPDATE Anniversaires SET Date="+str(date)+" WHERE User_ID="+str(user.id))
    connexion.commit()
    connexion.close()
    return
#Récupère l'anniversaire de l'utilisateur dans la base de donnée
def get_birthday(user : discord.User) -> str:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT Date FROM Anniversaires WHERE User_ID='"+str(user.id)+"'"
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    return (parse_date(result[0]))
#Formate la date pour pouvoir être utilisée
def parse_date(date : str) -> str:
    month : int = int(date) % 100
    month1 : int = month // 10
    month2 : int = month % 10
    day : int = int(date) // 100
    day1 : int = day // 10
    day2 : int = day % 10
    if ((day > 31) or (day < 1) or (month > 12) or (month < 1) or ((month == 2) and (day > 29)) or (((month == 4) or (month == 6) or (month == 9) or (month == 11)) and day > 30)):
        return ("00/00")
    parsed : str = str(day1)+str(day2)+"/"+str(month1)+str(month2)
    return (parsed)

#=============================================== BOOLÉENS ===================================================
#Vérifie si un anniversaire est stocké pour l'utilisateur
def check_birthday(user : discord.User) -> bool:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT User_ID FROM Anniversaires WHERE User_ID='"+str(user.id)+"'"
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    if (result):
        return True
    else:
        return False