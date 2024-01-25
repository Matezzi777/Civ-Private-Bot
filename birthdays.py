##################################################     INITIALISATION    ##################################################

#import des librairies
import discord
from discord.ext import commands
import sqlite3
import datetime



################################################## REQUÊTES ANNIVERSAIRE ##################################################

#Affiche la date (format : DD/MM/YYYY)
async def display_date(ctx : commands.Context):
    day = str(datetime.date.today())[8] + str(datetime.date.today())[9]
    month = str(datetime.date.today())[5] + str(datetime.date.today())[6]
    year = str(datetime.date.today())[0] + str(datetime.date.today())[1] + str(datetime.date.today())[2] + str(datetime.date.today())[3]
    await ctx.send("Today is : **"+day+"/"+month+"/"+year+"** (UTC + 1)")

#Ajoute un anniversaire dans la base de donnée
def add_birthday(user_id : int, date : int):
    if (check_birthday(user_id)):
        print("Birthday already in Database")
    else:
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request : str = "INSERT INTO Anniversaires (User_ID, Date) VALUES ("+str(user_id)+", "+str(date)+")"
        cursor.execute(request)
        connexion.commit()
        connexion.close()

#Supprime un anniversaire de la base de donnée
def rem_birthday(user_id : int):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "DELETE FROM Anniversaires WHERE User_id='"+str(user_id)+"'"
    cursor.execute(request)
    connexion.commit()
    connexion.close()

#Vérifie si un anniversaire est stocké pour l'utilisateur
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

#Récupère l'anniversaire de l'utilisateur dans la base de donnée
def get_birthday(user_id : int):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT Date FROM Anniversaires WHERE User_ID='"+str(user_id)+"'"
    cursor.execute(request)
    connexion.commit()
    result = cursor.fetchone()
    connexion.close()
    return (parse_date(result[0]))

#Formate la date pour pouvoir être utilisée
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

#Modifie la date d'anniversaire de l'utilisateur 
def change_birthday(user_id : int, date : str):
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    cursor.execute("UPDATE Anniversaires SET Date="+str(date)+" WHERE User_ID="+str(user_id))
    connexion.commit()
    connexion.close()

#Affiche les anniversaire stockés dans la base de donnée
async def display_birthdays(ctx : commands.Context):
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
            await ctx.send("**"+user.display_name+"** ----- **"+str(parse_date(row[1]))+"**")
    else:
        await ctx.send("Database empty.")



#===================================== IN PROGRESS BIRTHDAY AUTOMATION ======================================
        
# async def check_today_birthdays(ctx):
#     print("Checking for birthday ...")
#     today = parsed_day()
#     if (is_in_database(today)):
#         bday_channel = ctx.guild.get_channel(int(1199087236327669850))
#         connexion = sqlite3.connect('db.sqlite')
#         cursor = connexion.cursor()
#         request = "SELECT COUNT(User_ID) FROM Anniversaires WHERE Date='"+str(today)+"'"
#         cursor.execute(request)
#         connexion.commit()
#         nb_bday = int(cursor.fetchone()[0])
#         #Récupérer tous les membres dont c'est l'anniversaire.
#         request = "SELECT User_ID FROM Anniversaires WHERE Date='"+str(today)+"'"
#         cursor.execute(request)
#         connexion.commit()
#         result = cursor.fetchall()
#         for row in result:
#             await bday_channel.send(f"Hey guys ! Today is **<@{row[0]}>**'s birthday ! Enjoy your day !")
#         connexion.close()
#         return print(str(nb_bday)+" birthday found for today.")
#     else:
#         return print("No birthday found for today.\n")

# def is_in_database(date : str):
#     connexion = sqlite3.connect('db.sqlite')
#     cursor = connexion.cursor()
#     request = "SELECT Date FROM Anniversaires WHERE Date='"+str(date)+"'"
#     cursor.execute(request)
#     connexion.commit()
#     result = cursor.fetchone()
#     connexion.close()
#     if (result):
#         return True
#     else:
#         return False

# def parsed_day():
#     today = datetime.date.today()
#     today_parsed = str(today)[8] + str(today)[9] + str(today)[5] + str(today)[6]
#     return (today_parsed)
