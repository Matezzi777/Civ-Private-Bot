#============================================= INITIALISATION ===============================================
#Import des modules
import discord
import sqlite3
import datetime
from discord.ext import commands
from classes import BotEmbed, SuccessEmbed, ErrorEmbed

#=============================================== CALIBRAGE ==================================================
#Leaderboard's channel ID
leaderboard_channel_id = 1211156479269404692

#Elo initial attribué aux nouveaux utilisateurs
elo_new_player = 1200
#Différence d'elo nécessaire pour avoir 90% de chances de victoire estimées
theta = 400

#========================================= COMMANDES PRINCIPALES ============================================
#$report @X @Y @Z
async def valid_report(bot : commands.Bot, liste_players : list) -> None:

    nb_players : int = len(liste_players)
    actual_elos : list= []

    print("")

    i : int = 0
    while (i < nb_players):
        user : discord.User = liste_players[i]
        if (not is_player_in_database(user)):
            add_u(user)
        actual_elos.append(get_elo(user))
        i = i + 1

    print("")

    i = 0
    while (i < nb_players):
        user : discord.User = liste_players[i]
        if (i == 0):
            update_top1(user)
            update_wins(user)
        elif (i < ((nb_players//2)) and nb_players >= 4):
            update_wins(user)
        else:
            update_lost(user)

        update_date(user)
        print("")
        i = i + 1
    
    i = 0
    while (i < nb_players):
        user : discord.User = liste_players[i]
        actual_elo : int = actual_elos[i]
        elo_variation : int = 0
        games_played_by_user = get_games_played(user)

        if (actual_elo >= 2300):
            max_change : int = 10
        elif (games_played_by_user <= 15):
            max_change : int = 40
        else:
            max_change : int = 20

        j : int = 0
        while (j < nb_players):
            if (i != j):
            
                if (i < j):
                    result = 1
                else:
                    result = 0
            
                opponent_elo : int = actual_elos[j]

                delta : int = actual_elo - opponent_elo
                proba_to_win : float = 1 / (1 + 10**(-delta/theta))
                elo_variation = elo_variation + max_change * (result - proba_to_win)

            j = j + 1

        elo_variation : int = elo_variation/(nb_players-1)
        new_elo : int = round(actual_elo + elo_variation)
        update_elo(user, new_elo)
        i = i + 1
    print("")
    print(f"===== Result validated =====")
    await update_scoreboard(bot)
    return
#Affiche le tableau des scores
async def display_scoreboard(ctx : commands.Context) -> None:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT User_ID, Elo, Top1, Wins, Lost FROM Ranked ORDER BY Elo DESC"
    cursor.execute(request)
    connexion.commit()
    result : list = cursor.fetchall()
    connexion.close()
    if (not result):
        embed=ErrorEmbed(description="For now, any game has been reported. If you have a game to report, use $report.")
        await ctx.send(embed=embed)
        return
    embed=BotEmbed(title="LEADERBOARD CIV PRIVATE CLUB SEASON #1", description="Here is the actual leaderboard for the 1st Ranked season of the Civ Private Club")
    i : int = 0
    nb_users_stored = len(result)
    while (i < nb_users_stored):
        embed.add_field(name="", value=f"**{i+1}.** <@{result[i][0]}>\n`Games played :` {result[i][3]+result[i][4]}\n`Ratio        :` {round(float(float(result[i][3])/float(result[i][3]+result[i][4])), 2)}\n`Elo          :` {result[i][1]}\n`Top 1        :` {result[i][2]}\n`Wins         :` {result[i][3]}\n`Lost         :` {result[i][4]}", inline=True)
        i = i + 1
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=30)
    return 

#============================================== LEADERBOARD =================================================
async def update_scoreboard(bot : commands.Bot) -> None:
    channel : discord.TextChannel = bot.get_channel(leaderboard_channel_id)
    async for message in channel.history(limit=12):
        await message.delete()
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = "SELECT User_ID, Elo, Top1, Wins, Lost FROM Ranked ORDER BY Elo DESC"
    cursor.execute(request)
    connexion.commit()
    result : list = cursor.fetchall()
    connexion.close()
    message = "## LEADERBOARD\n`Rank   Skill   [wins - loss]   win%   Top1`"
    await channel.send(message)
    message = ""
    if (not result):
        i : int = 0
        while (i < 3):
            j : int = 0
            while (j < 10):
                message = message + f"`{parsed_rank((i*10)+j+1)}    ----    [   X - X   ]    --%   -   `\n"
                j = j + 1
            await channel.send(message)
            message = ""
            i = i + 1

    else:
        nb_players_in_database : int = len(result)
        i : int = 0
        while ((i <= nb_players_in_database // 10) and (i < 10)):
            j : int = 0
            while (j < 10):
                n : int = i*10 + j
                if (n < nb_players_in_database):
                    user_id : int = result[n][0]
                    elo : int = result[n][1]
                    top1 : int = result[n][2]
                    wins : int = result[n][3]
                    lost : int = result[n][4]
                    winrate = round((float(wins)/float(wins+lost)) * 100)
                    message = message + f"`{parsed_rank(n+1)}    {parsed_skill(elo)}    [ {parsed_wins(wins)} - {parsed_lost(lost)} ]   {parsed_winrate(winrate)}   {parsed_top1(top1)}`  <@{user_id}>\n"
                else:
                    message = message + f"`{parsed_rank(n+1)}    ----    [   X - X   ]    --%   -   `\n"
                j = j + 1
            await channel.send(message)
            message = ""
            i = i + 1
    print(f"Leaderboard updated in #{channel.name}")
    return

def parsed_rank(n : int) -> str:
    if (n <= 9):
        return (f"#{n} ")
    else:
        return (f"#{n}")

def parsed_skill(skill : int) -> str:
    if (skill <= 9):
        return (f"{   skill}")
    elif (skill <= 99):
        return (f"{  skill}")
    elif (skill <= 999):
        return (f"{ skill}")
    else:
        return (f"{skill}")

def parsed_wins(wins : int) -> str:
    if (wins <= 9):
        return (f"  {wins}")
    elif (wins <= 99):
        return (f" {wins}")
    else:
        return (f"{wins}")

def parsed_lost(lost : int) -> str:
    if (lost <= 9):
        return (f"{lost}  ")
    elif (lost <= 99):
        return (f"{lost} ")
    else:
        return (f"{lost}")

def parsed_winrate(winrate : int) -> str:
    if (winrate == 100):
        return (f"{winrate}%")
    elif (winrate <= 9):
        return (f"  {winrate}%")
    else:
        return (f" {winrate}%")

def parsed_top1(top1 : int) -> str:
    if (top1 <= 9):
        return (f"{top1}   ")
    elif(top1 <= 99):
        return (f"{top1}  ")
    elif(top1 <= 999):
        return (f"{top1} ")
    else:
        return (f"{top1}")

#======================================= BASE DE DONNÉE (LECTURE) ===========================================
#Récupère le nombre de parties jouées par l'utilisateur
def get_games_played(user : discord.User) -> int:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request_get_win : str = f"SELECT Wins FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request_get_win)
    wins : int = cursor.fetchone()[0]
    request_get_lost : str = f"SELECT Lost FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request_get_lost)
    lost : int = cursor.fetchone()[0]
    games_played : int = wins + lost
    connexion.close()
    return (games_played)
#Récupère l'elo de l'utilisateur
def get_elo(user : discord.User) -> int:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Elo FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result : int = cursor.fetchone()[0]
    connexion.close()
    return (result)
#Récupère le nombre de top 1 de l'utilisateur
def get_top1(user : discord.User) -> int:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Top1 FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result : int = cursor.fetchone()[0]
    connexion.close()
    return (result)
#Récupère le nombre de wins de l'utilisateur
def get_wins(user : discord.User) -> int:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Wins FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result : int = cursor.fetchone()[0]
    connexion.close()
    return (result)
#Récupère le nombre de défaites de l'utilisateur
def get_lost(user : discord.User) -> int:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Lost FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result : int = cursor.fetchone()[0]
    connexion.close()
    return (result)
#Récupère la date de la dernière partie jouée par l'utilisateur
def get_date(user : discord.User) -> str:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Date FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result : int = cursor.fetchone()[0]
    date : str = str(result//1000)+str((result%1000)//100)+"/"+str((result%100)//10)+str(result%10)
    connexion.close()
    return (date)

#====================================== BASE DE DONNÉE (ÉCRITURE) ===========================================
#Ajoute l'utilisateur à la base de donnée
def add_u(user : discord.User) -> int:
    if (is_player_in_database(user)):
        print(f"{user.name} already stored in the database.")
        return (0)
    else:
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request : str = f"INSERT INTO Ranked VALUES ('{user.id}', {elo_new_player}, 0, 0, 0, 0)"
        cursor.execute(request)
        connexion.commit()
        connexion.close()
        if (is_player_in_database(user)):
            print(f"{user.name} added to the database.")
            return (1)
        else:
            print(f"Error in the INSERT request.")
            return (0)
#Supprime l'utilisateur de la base de donnée
def rm_u(user : discord.User) -> int:
    if (is_player_in_database(user)):
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request : str = f"DELETE FROM Ranked WHERE User_ID='{user.id}'"
        cursor.execute(request)
        connexion.commit()
        connexion.close()
        if (not is_player_in_database(user)):
            print(f"{user.name} removed from the database.")
            return (1)
        else:
            print(f"Error in the DELETE request.")
            return (0)
    else:
        print(f"Impossible to delete the user.\n{user.name} not found in the database.")
        return (0)
#Reset la base de donnée Ranked
def rm_all_users() -> int:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"DELETE FROM Ranked"
    cursor.execute(request)
    connexion.commit()
    connexion.close()
    result = is_database_empty()
    if (result):
        print(f"Database cleared.")
        return (1)
    else:
        print(f"Error during the database clearing process.")
        return (0)

#Met à jour l'elo de l'utilisateur
def update_elo(user : discord.User, new_elo : int) -> None:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request_write : str = f"UPDATE Ranked SET Elo={new_elo} WHERE User_ID='{user.id}'"
    cursor.execute(request_write)
    connexion.commit()
    connexion.close()
    print(f"{user.name}'s Elo updated.")
    return
#Incrémente les top 1 de l'utilisateur
def update_top1(user : discord.User) -> None:
    connexion = sqlite3.connect("db.sqlite")
    cursor = connexion.cursor()
    request_get : str = f"SELECT Top1 FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request_get)
    top1 : int = cursor.fetchone()[0]
    top1 = top1 + 1
    request_write : str = f"UPDATE Ranked SET Top1={top1} WHERE User_ID='{user.id}'"
    cursor.execute(request_write)
    connexion.commit()
    connexion.close()
    print(f"{user.name}'s Top1 updated.")
    return
#Incrémente les wins de l'utilisateur
def update_wins(user : discord.User) -> None:
    connexion = sqlite3.connect("db.sqlite")
    cursor = connexion.cursor()
    request_get : str = f"SELECT Wins FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request_get)
    wins : int = cursor.fetchone()[0]
    wins = wins + 1
    request_write : str = f"UPDATE Ranked SET Wins={wins} WHERE User_ID='{user.id}'"
    cursor.execute(request_write)
    connexion.commit()
    connexion.close()
    print(f"{user.name}'s Wins updated.")
    return
#Incrémente les défaites de l'utilisateur
def update_lost(user : discord.User) -> None:
    connexion = sqlite3.connect("db.sqlite")
    cursor = connexion.cursor()
    request_get : str = f"SELECT Lost FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request_get)
    lost : int = cursor.fetchone()[0]
    lost = lost + 1
    request_write : str = f"UPDATE Ranked SET Lost={lost} WHERE User_ID='{user.id}'"
    cursor.execute(request_write)
    connexion.commit()
    connexion.close()
    print(f"{user.name}'s Lost updated.")
    return
#Met à jour la date de la dernière partie jouée par l'utilisateur à aujourd'hui
def update_date(user : discord.User) -> None:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    day = str(datetime.date.today())[8] + str(datetime.date.today())[9]
    month = str(datetime.date.today())[5] + str(datetime.date.today())[6]
    date : int = int(day+month)
    request_write : str = f"UPDATE Ranked SET Date={date} WHERE User_ID={user.id}"
    cursor.execute(request_write)
    connexion.commit()
    connexion.close()
    print(f"{user.name}'s Date updated.")
    return

#=============================================== BOOLÉENS ===================================================
#Vérifie la présence de l'utilisateur dans la base de donnée
def is_player_in_database(user : discord.User) -> bool:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT * FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    result : int = cursor.fetchone()
    connexion.close()
    if result:
        return True
    else:
        return False
#Vérifie la présence de l'utilisateur dans la liste d'utilisateurs donnée
def is_in_list(user : discord.User, liste : list) -> bool:
    i : int = 0
    while (i < len(liste)):
        if (user == liste[i]):
            return True
        i = i + 1
    return False
#Vérifie si la base de donnée est vide
def is_database_empty() -> bool:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT * FROM Ranked"
    cursor.execute(request)
    connexion.commit()
    result : list = cursor.fetchall()
    connexion.close()
    if (not result):
        return True
    else:
        return False