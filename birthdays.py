##################################################     INITIALISATION    ##################################################

#import des librairies
import discord
from discord.ext import commands
import sqlite3

#définition d'objets utiles
bot = commands.Bot(command_prefix="$",intents=discord.Intents.all(),description="$mapvote or $serverinfo.")

################################################## REQUÊTES ANNIVERSAIRE ##################################################

#Ajoute un anniversaire à la base de donnée
def add_birthday(user_id : int, date : int):
    if (check_birthday(user_id)):
        print("Birthday already in Database")
    else:
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        cursor.execute("""INSERT INTO Anniversaires (User_ID, Date) VALUES (?, ?)""", (user_id, date))
        connexion.commit()
        connexion.close()

def check_birthday(user_id : int):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT User_ID FROM Anniversaires WHERE User_ID='"+str(user_id)+"'"
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    if (result):
        return True
    else:
        return False
    
def get_birthday(user_id : int):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT Date FROM Anniversaires WHERE User_ID='"+str(user_id)+"'"
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    return (parse_date(result[0]))
    
def parse_date(date : str):
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

def change_birthday(user_id : int, date : str):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    cursor.execute("UPDATE Anniversaires SET Date="+str(date)+" WHERE User_ID="+str(user_id))
    connexion.commit()
    connexion.close()

    return

async def display_birthdays(ctx):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT User_ID, Date FROM Anniversaires"
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchall()
    connexion.close()
    if(result):
        for row in result:
            user = ctx.guild.get_member(row[0])
            # await ctx.send(user.mention+" <"+str(row[0])+"> | Date :"+str(row[1]))
            await ctx.send("**"+user.display_name+"** ----- **"+str(parse_date(row[1]))+"**")
    else:
        await ctx.send("Database empty.")