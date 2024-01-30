##################################################     INITIALISATION    ##################################################

import discord
import sqlite3
import datetime
from discord.ext import commands
from classes import CivPrivateBotEmbed

elo_new_player = 1200
theta = 400

###########################################################################################################################

#Report
    #1v1
    #FFA
    #Teamer

#$report @X @Y @Z
async def valid_report(liste_players : list):

    nb_players : int = len(liste_players)
    actual_elos : list= []

    print("")

    i : int = 0
    while (i < nb_players):
        user : discord.User = liste_players[i]
        if (not is_player_in_database(user)):
            add_user(user)
        actual_elos.append(get_elo(user))
        i = i + 1

    print("")

    i = 0
    while (i < nb_players):
        user : discord.User = liste_players[i]
        if (i == 0):
            update_top1(user)
            update_wins(user)
        elif (i < (nb_players//2)):
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
    return print(f"===== Result validated =====")


async def display_scoreboard(ctx : commands.Context) -> None:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT User_ID, Elo, Top1, Wins, Lost FROM Ranked ORDER BY Elo DESC"
    cursor.execute(request)
    connexion.commit()
    result : list = cursor.fetchall()
    if (not result):
        embed=CivPrivateBotEmbed(colour=discord.Colour.red(), title="Database empty", description="For now, any game has been reported. If you have a game to report, use $report.")
        await ctx.send(embed=embed)
        return
    embed=CivPrivateBotEmbed(title="LEADERBOARD CIV PRIVATE CLUB SEASON #1", description="Here is the actual leaderboard for the 1st Ranked season of the Civ Private Club")
    i : int = 0
    nb_users_stored = len(result)
    while (i < nb_users_stored):
        embed.add_field(name="", value=f"**{i+1} : <@{result[i][0]}>** | Elo : **{result[i][1]}** | Top 1 : **{result[i][2]}** | Wins : **{result[i][3]}** | Lost : **{result[i][4]}**", inline=False)
        i = i + 1
    await ctx.send(embed=embed)
    return 

###########################################################################################################################

#Stats

def get_top1(user : discord.User) -> int:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Top1 FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result : int = cursor.fetchone()[0]
    connexion.close()
    return (result)

def get_wins(user : discord.User) -> int:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Wins FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result : int = cursor.fetchone()[0]
    connexion.close()
    return (result)

def get_lost(user : discord.User) -> int:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Lost FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result : int = cursor.fetchone()[0]
    connexion.close()
    return (result)

def get_date(user : discord.User) -> str:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Date FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result : int = cursor.fetchone()[0]
    date : str = str(result//1000)+str((result%1000)//100)+"/"+str((result%100)//10)+str(result%10)
    return (date)

###########################################################################################################################
def get_elo(user : discord.User) -> int:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request : str = f"SELECT Elo FROM Ranked WHERE User_ID='{user.id}'"
    cursor.execute(request)
    connexion.commit()
    result : int = cursor.fetchone()[0]
    connexion.close()
    return (result)

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
    
def add_user(user : discord.User) -> None:
    if (is_player_in_database(user)):
        print(f"{user.name} already stored in the database.")
        return
    else:
        connexion = sqlite3.connect('db.sqlite')
        cursor = connexion.cursor()
        request : str = f"INSERT INTO Ranked VALUES ('{user.id}', {elo_new_player}, 0, 0, 0, 0)"
        cursor.execute(request)
        connexion.commit()
        connexion.close()
        print(f"{user.name} added to the database.")
        return

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
    return (games_played)

def update_elo(user : discord.User, new_elo : int) -> None:
    connexion = sqlite3.connect('db.sqlite')
    cursor = connexion.cursor()
    request_write : str = f"UPDATE Ranked SET Elo={new_elo} WHERE User_ID='{user.id}'"
    cursor.execute(request_write)
    connexion.commit()
    connexion.close()
    print(f"{user.name}'s Elo updated.")
    return