#============================================= INITIALISATION ===============================================
#Import des modules
import discord
import discord.ext
from discord.ui import Button, View
from birthdays import *
from draft import *
from mapvote import *
from ranked import *
from classes import Bot, CivPrivateBotEmbed
from tokens import TOKEN

#Définition du bot
bot = Bot()
#Définition de boutons utiles
button_yes = Button(label="Yes", style=discord.ButtonStyle.green)
button_no = Button(label="No", style=discord.ButtonStyle.red)
button_change = Button(label="Yes", style=discord.ButtonStyle.green)

#============================================= CLASSES REPORT ===============================================
#View $report
class ReportView(discord.ui.View):
    def __init__(self, liste_players) -> None:
        super().__init__()
        self.liste_players = liste_players
        self.add_item(ReportButton(liste_players))
#Bouton validation $report
class ReportButton(discord.ui.Button):
    def __init__(self, liste_players : list) -> None:
        super().__init__(
            label="✅ Confirm",
            style=discord.ButtonStyle.green
        )
        self.liste_players : list = liste_players
        self.count = 0
        self.users_who_clicked : list = []
        i : int = 0
        print("\n===== Users in the game : =====")
        while (i < len(self.liste_players)):
            print(f"{self.liste_players[i].name}")
            i = i + 1
        print("")
    async def callback(self, interaction : discord.Interaction) -> None:
        if (interaction.user.id == 866997795993944084):
            needed_confirm = 1
        elif (len(self.liste_players) == 2):
            needed_confirm = 2
        else:
            needed_confirm = 3

        if (is_in_list(interaction.user, self.liste_players) or interaction.user.id == 866997795993944084): #Si l'utilisateur était dans la partie ou que Matezzi valide la partie.
            if (not is_in_list(interaction.user, self.users_who_clicked)): #Si il n'a pas déjà cliqué
                self.count = self.count + 1
                self.users_who_clicked.append(interaction.user)
                print(f"{interaction.user.name} confirmed the reported result.")
            else: #Si il a déjà cliqué
                print(f"{interaction.user.name} already clicked.")

        else: #Si l'utilisateur n'était pas dans la partie.
            print(f"{interaction.user.name} clicked but wasn't on the game.")

        if (self.count >= needed_confirm):
            self.label="Report validated"
            self.disabled=True
            await valid_report(self.liste_players)
            embed=CivPrivateBotEmbed(colour=discord.Colour.green(), title="Result confirmed", description="Result confirmed, result stored in the database and player's stats updated.")
            await interaction.response.edit_message(view=self.view)
            await interaction.followup.send(embed=embed)
        else:
            self.label=f"{needed_confirm-self.count} more ✅ needed"
            await interaction.response.edit_message(view=self.view)

#============================================ COMMANDES INFOS ===============================================
#$ping
@bot.command()
async def ping(ctx : commands.Context) -> None:
    embed = discord.Embed(colour=discord.Colour.green(), title="PONG")
    await ctx.send(embed=embed)
#$hello
@bot.command()
async def hello(ctx : commands.Context) -> None:
    server = ctx.guild
    embed = CivPrivateBotEmbed(title="Hello *Civ enjoyer !*", description=f"Let me introduce myself...\nMy name is **Civ Private Bot** (but you can call me CPB), I try my best to add some useful tools on the **{server.name}**, like $mapvote, $draft.\n\nWe actualy are working on an elo ranking system 😉\n\nPlease message <@866997795993944084> if you have any suggestions or feedback !")
    await ctx.send(embed=embed)
#$serverinfo
@bot.command()
async def serverinfo(ctx : commands.Context) -> None:
    server = ctx.guild
    embed = CivPrivateBotEmbed(title=f"{server.name}", description=f"Are you tired about leavers in Civ 6 Multiplayer ?\nAre you tired about the 3k gametime player bullying you ?\n\nWelcome to the {server.name} !\n\nNo worries, you are at the good place. This discord exists to gather a community of nice peoples who want to play civ, learn civ and discuss about civ !\n\nIf you are new here, don't worry, I'm sure you'll find what you are looking for.")
    embed.add_field(name="Some stats about us :", value =f"Members : **{server.member_count}**\nText Channels : {len(server.text_channels)}\nVoice Channels : {len(server.voice_channels)}", inline=False)
    embed.add_field(name="", value=f"Created by <@866997795993944084> and <@828975075951902733> the {server.created_at.date()}", inline=False)
    await ctx.send(embed=embed)
#$clear X
@bot.command()
async def clear(ctx : commands.Context, nombre : int) -> None:
    async for message in ctx.channel.history(limit=nombre+1):
        print(message)
        await message.delete()
#$datenow
@bot.command()
async def datenow(ctx : commands.Context) -> None:
    await display_date(ctx)

#========================================== COMMANDES PRE - GAME ============================================
#$draft 2.0
@bot.command()
async def draft(ctx : commands.Context, nb_civs : int) -> None:
    await make_draft(ctx, nb_civs)  
#$blind_draft
@bot.command()
async def blind_draft(ctx : commands.Context, nb_civs : int) -> None:
    await make_blind_draft(ctx, nb_civs)
#$draft X Y
@bot.command()
async def generic_draft(ctx : commands.Context, players : int, nb_civs : int) -> None:
    await make_generic_draft(ctx, players, nb_civs)

#$mapvote v2
@bot.command()
async def mapvote(ctx : commands.Context) -> None:
    await make_mapvote(ctx)
#$generic_mapvote
@bot.command()
async def generic_mapvote(ctx : commands.Context) -> None:
    await make_generic_mapvote(ctx)

#========================================== COMMANDES BIRTHDAYS =============================================
#$set_birthday DDMM
@bot.command()
async def set_birthday(ctx : commands.Context, date : str) -> None:
    yesno = View()
    yesno.add_item(button_yes)
    yesno.add_item(button_no)
    user = ctx.message.author
    date_parsed = parse_date(date)
    if (date_parsed == "00/00"):
        embed= discord.Embed(colour=discord.Colour.red(), title="Process aborted", description="Wrong date format.\nUse the following format : DD/MM.")
        return await ctx.send(embed=embed, delete_after=7)
    if (check_birthday(user)):
        actual_birthday = get_birthday(user)
        if (actual_birthday == date_parsed):
            embed= discord.Embed(colour=discord.Colour.red(), title="Process aborted", description=f"Your birthday is already stored in the database at **{actual_birthday}** (DD/MM).")
            return await ctx.send(embed=embed, delete_after=7)
        else:
            async def button_yes_callback(interaction : discord.Interaction):
                change_birthday(user, date)
                embed= discord.Embed(colour=discord.Colour.green(), title="Success", description=f"Date modified.")
                return await interaction.response.send_message(embed=embed)
            async def button_no_callback(interaction : discord.Interaction):
                embed= discord.Embed(colour=discord.Colour.red(), title="Process aborted", description=f"Date not modified.")
                return await interaction.response.send_message(embed=embed)
            button_yes.callback = button_yes_callback
            button_no.callback = button_no_callback
            embed= CivPrivateBotEmbed(title="Modify birthday ?", description=f"Your birthday is already stored in the database at **{actual_birthday}** (DD/MM).\n\nDo you want to change it for *{date_parsed}* ?")
            return await ctx.send(embed=embed, view=yesno, delete_after=7)
    else:
        async def button_yes_callback(interaction : discord.Interaction):
            add_birthday(user, date)
            embed= discord.Embed(colour=discord.Colour.green(), title="Success", description="Birthday added.")
            return await interaction.response.send_message(embed=embed)
        async def button_no_callback(interaction : discord.Interaction):
            embed= discord.Embed(colour=discord.Colour.red(), title="Process aborted", description="Birthday not added.")
            return await interaction.response.send_message(embed=embed)
        button_yes.callback = button_yes_callback
        button_no.callback = button_no_callback
        embed=CivPrivateBotEmbed(title="Add birthday ?", description=f"You birthday is not on the database.\n\nDo you want to set it to *{date_parsed}* ?")
        await ctx.send(embed=embed, view=yesno, delete_after=7)
#$rem_birthday
@bot.command()
async def rm_birthday(ctx : commands.Context) -> None:
    yesno = View()
    yesno.add_item(button_yes)
    yesno.add_item(button_no)
    user = ctx.message.author
    if (check_birthday(user)):
        async def button_yes_callback(interaction : discord.Interaction):
            rem_birthday(user)
            embed= discord.Embed(colour=discord.Colour.green(), title="Success", description=f"Birthday deleted from database.")
            return await interaction.response.send_message(embed=embed)
        async def button_no_callback(interaction : discord.Interaction):
            embed= discord.Embed(colour=discord.Colour.red(), title="Process aborted", description=f"Birthday still stored in the database.")
            return await interaction.response.send_message(embed=embed)
        button_yes.callback = button_yes_callback
        button_no.callback = button_no_callback
        embed= CivPrivateBotEmbed(title="Remove birthday ?", description="Do you really want to remove your birthday from the database ?")
        return await ctx.send(embed=embed, view=yesno, delete_after=10)
    else:
        embed= discord.Embed(colour=discord.Colour.red(), title="Process aborted", description="No birthday found in the database for you.")
        return await ctx.send(embed=embed)
#$birthdays
@bot.command()
async def birthdays(ctx : commands.Context) -> None:
    await display_birthdays(ctx)

#=========================================== COMMANDES RANKED ===============================================
#$report @First @Second @Third ...
@bot.command()
async def report(ctx : commands.Context, *args : discord.User) -> None:
    if (len(args) < 2):
        embed=CivPrivateBotEmbed(colour=discord.Colour.red(), title="Process aborted", description="Not enough players in the game reported (minimum 2)")
        return await ctx.send(embed=embed)
    embed=CivPrivateBotEmbed(title="Verify the Result", description="Please make sure the result reported is correct before verifying it.\nThe report needs to be confirmed by 3 different players (2 for a 1v1).")
    i : int = 0
    message = ""
    while (i < len(args)):
        message = message + f"**{i+1} :** {args[i].name}\n"
        i = i + 1
    embed.add_field(name="Result reported :", value=message)
    view=ReportView(args)
    await ctx.send(embed=embed, view=view)
#$stats
@bot.command()
async def stats(ctx : commands.Context) -> None:
    user : discord.User = ctx.message.author
    if (not is_player_in_database(user)):
        embed=CivPrivateBotEmbed(colour=discord.Colour.red(), title="User not found", description=f"<@{user.id}> not found in the database.\nPlease report a game with this player to create an entry.")
        return await ctx.send(embed=embed)
    elo : int = get_elo(user)
    top1 : int = get_top1(user)
    wins : int = get_wins(user)
    lost : int = get_lost(user)
    date : str = get_date(user)
    embed=CivPrivateBotEmbed(title="STATS", description=f"<@{user.id}>")
    embed.set_thumbnail(url=user.avatar)
    embed.add_field(name="", value=f"**Games played : {wins+lost}\nElo : {elo}\nTop 1 : {top1}\nWins : {wins}\nLost : {lost}\nLast game played : {date}**")
    return await ctx.send(embed=embed)
#$scoreboard
@bot.command()
async def leaderboard(ctx : commands.Context) -> None:
    await display_scoreboard(ctx)
    return
#$setup_leaderboard
@bot.command()
async def setup_leaderboard(ctx: commands.Context) -> None:
    channel = bot.get_channel(1204872785642389575)
    await setup_scoreboard(ctx, channel)
    return

#================================================== RUN =====================================================
#Run le bot
bot.run(TOKEN)
