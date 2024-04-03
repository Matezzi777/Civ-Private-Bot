#           ______  __  __  __      ______  ______   __  __  __  ____   _________  ______      _____    _______  _________
#          / ____/ / / / / / /     / __  / / __  /  / / / / / / / _  | /___  ___/ / ____/     / __  |  / ___  / /___  ___/
#         / /     / / / / / /     / /_/ / / /_/ /  / / / / / / / /_| |    / /    / /_        / /_/ /  / /  / /     / /
#        / /     / / | | / /     /  ___/ / __  /  / / | | / / / ___  |   / /    / __/       / ___ |  / /  / /     / /
#       / /___  / /  | |/ /     / /     / / | |  / /  | |/ / / /  / /   / /    / /___      / /__/ / / /__/ /     / /
#      /_____/ /_/   |___/     /_/     /_/  /_/ /_/   |___/ /_/  /_/   /_/    /_____/     /______/ /______/     /_/

#============================================= INITIALISATION ===============================================
#Import des modules
import discord
import discord.ext
import datetime
from discord.ui import Button, View
from birthdays import *
from draft import *
from mapvote import *
from ranked import *
from civilopedia import *
from classes import Bot, BotEmbed, SuccessEmbed, ErrorEmbed, ValidButton
from tokens import TOKEN

#Définition du bot
bot = Bot()
#Définition de boutons utiles
button_yes = Button(label="Yes", style=discord.ButtonStyle.green)
button_no = Button(label="No", style=discord.ButtonStyle.red)
button_change = Button(label="Yes", style=discord.ButtonStyle.green)

#=============================================== CONSTANTS ==================================================
welcome_channel_id = 1211150113477627955

#============================================= CLASSES REPORT ===============================================
#View $report
class ReportView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        if (self.nb_users == 2):
            self.needed_confirm : int = 2
            self.add_item(ReportButton(users, self.needed_confirm))
        elif (self.nb_users > 2):
            self.needed_confirm : int = 3
            self.add_item(ReportButton(users, self.needed_confirm))
        else:
            print(f"Erreur nombre d'arguments. ({self.nb_users}/2+)")
#Bouton validation $report
class ReportButton(discord.ui.Button):
    def __init__(self, users : list, needed_confirm) -> None:
        super().__init__(
            label="✅ Confirm",
            style=discord.ButtonStyle.green
        )
        self.users : list = users
        self.needed_confirm = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []
        i : int = 0
        message : str = "  Players in the game :"
        while (i < len(self.users)):
            message = message + f" @{self.users[i].name}"
            i = i + 1
        print(message)

    async def callback(self, interaction : discord.Interaction) -> None:
        if (interaction.user.id == 866997795993944084): #Si admin
            print(f"  @{interaction.user.name} confirmed.")
            #Remplace par ValidButton
            valid_button : discord.Button = ValidButton()
            valid_button.label = "✅ Game reported"
            valid_view = discord.ui.View()
            valid_view.add_item(valid_button)
            await interaction.response.edit_message(view=valid_view)

            #Message retour
            embed=SuccessEmbed(description="Result confirmed, result stored in the database and player's stats updated.")
            await interaction.followup.send(embed=embed)

            #valid()
            await valid_report(bot, self.users)
            return
        
        else: #Si non-admin
            if (is_in_list(interaction.user, self.users)): #Si l'utilisateur était dans la partie
                if (is_in_list(interaction.user, self.users_who_clicked)): #Si l'utilisateur a déjà cliqué
                    print(f"    @{interaction.user.name} already confirmed.") #Console : L'utilisateur a déjà cliqué
                    embed = ErrorEmbed(description="You already confirmed this report.")
                    await interaction.response.send_message(embed=embed, ephemeral=True)

                else: #Si l'utilisateur n'a pas encore cliqué
                    self.count = self.count + 1 #+1 clic
                    self.users_who_clicked.append(interaction.user)
                    print(f"  @{interaction.user.name} confirmed.") #Console : Clic enregistré
                    embed = SuccessEmbed(title="YOU CONFIRMED THIS REPORT")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            
            else: #Si l'utilisateur n'était pas dans la partie
                embed = ErrorEmbed(description="You tried to confirm a report which does not concern you.") #Créé le message d'erreur
                await interaction.response.send_message(embed=embed, ephemeral=True) #Envoie un MP d'erreur à l'utilisateur
                print(f"    @{interaction.user.name} tried to confirm.")
        
        if (self.count == self.needed_confirm): #Si le nombre de clics est atteint
            #valid()
            await valid_report(bot, self.users)
            #Remplace par ValidButton
            valid_button : discord.Button = ValidButton()
            valid_button.label = "✅ Game reported"
            valid_view = discord.ui.View()
            valid_view.add_item(valid_button)
            await interaction.response.edit_message(view=valid_view)
            return
        
        else: #Si le nombre de clics n'est pas atteint
            #Met à jour le bouton
            self.label=f"{self.needed_confirm-self.count} more ✅ needed"
            await interaction.response.edit_message(view=self.view)
            return

class LFGButtonYes(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="✅ Count me in",
            style=discord.ButtonStyle.green
        )

    async def callback(self, interaction : discord.Interaction) -> None:
        if (interaction.user in self.view.users): #Si l'utilisateur a déjà cliqué
            self.view.users.remove(interaction.user)
        else: #Si l'utilisateur n'a pas encore cliqué
            if (interaction.user in self.view.maybe): #Si l'utilisateur a déjà cliqué sur Maybe
                self.view.maybe.remove(interaction.user)
            self.view.users.append(interaction.user)
        will_play : str = f""
        maybe : str = f""
        i : int = 0
        while (i < len(self.view.users)):
            will_play = will_play + f"{self.view.users[i].mention}\n"
            i = i + 1
        i = 0
        while (i < len(self.view.maybe)):
            maybe = maybe + f"{self.view.maybe[i].mention}\n"
            i = i + 1
        embed = BotEmbed(title="LOOKING FOR GAME", description="Game starting soon !\nClick ✅ if you participate.\nClick ❔ if you're not sure.")
        embed.add_field(name="✅ Will play :", value=will_play, inline=False)
        embed.add_field(name="❔ Maybe :", value=maybe, inline=False)
        await interaction.response.edit_message(embed=embed, view=self.view)
        return

class LFGButtonMaybe(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="❔ Maybe",
            style=discord.ButtonStyle.grey
        )

    async def callback(self, interaction : discord.Interaction) -> None:
        if (interaction.user in self.view.maybe): #Si l'utilisateur a déjà cliqué
            self.view.maybe.remove(interaction.user)
        else: #Si l'utilisateur n'a pas encore cliqué
            if (interaction.user in self.view.users): #Si l'utilisateur a déjà cliqué sur Maybe
                self.view.users.remove(interaction.user)
            self.view.maybe.append(interaction.user)
        will_play : str = f""
        maybe : str = f""
        i : int = 0
        while (i < len(self.view.users)):
            will_play = will_play + f"{self.view.users[i].mention}\n"
            i = i + 1
        i = 0
        while (i < len(self.view.maybe)):
            maybe = maybe + f"{self.view.maybe[i].mention}\n"
            i = i + 1
        embed = BotEmbed(title="LOOKING FOR GAME", description="Game starting soon !\nClick ✅ if you participate.\nClick ❔ if you're not sure.")
        embed.add_field(name="✅ Will play :", value=will_play, inline=False)
        embed.add_field(name="❔ Maybe :", value=maybe, inline=False)
        await interaction.response.edit_message(embed=embed, view=self.view)
        return

class LFGView(discord.ui.View):
    def __init__(self, caller : discord.User) -> None:
        super().__init__(timeout=None)
        self.users : list[discord.User] = []
        self.maybe : list[discord.User] = []
        self.users.append(caller)
        self.add_item(LFGButtonYes())
        self.add_item(LFGButtonMaybe())

#================================================ EVENTS ====================================================

@bot.event
async def on_message(message : discord.Message):
    await bot.process_commands(message)
    channel = message.channel
    if (channel.id == welcome_channel_id):
        await message.add_reaction("👋")
        print(f"New member joined\n  {datetime.datetime.now()}\n")
    return

#============================================ COMMANDES INFOS ===============================================
#$ping
@bot.command(aliases=['p', 'pong'],
        help="Respond PONG if the bot is running.",
        description="PING",
        brief="- Pong",
        enabled=True,
        hidden=False)
async def ping(ctx : commands.Context) -> None:
    print(f"\n$ping used by @{ctx.message.author.name} in #{ctx.channel.name}")
    embed = SuccessEmbed(title="PONG")
    embed.remove_footer()
    await ctx.send(embed=embed)
#$hello
@bot.command(aliases=['h'],
        help="Let me introduce myself !",
        description="HELLO",
        brief="- Some introductions",
        enabled=True,
        hidden=False)
async def hello(ctx : commands.Context) -> None:
    print(f"\n$hello used by @{ctx.message.author.name} in #{ctx.channel.name}")
    server = ctx.guild
    embed = BotEmbed(title="Hello *Civ enjoyer !*", description=f"Let me introduce myself...\nMy name is **Civ Private Bot** (but you can call me CPB), I try my best to add some useful tools on the **{server.name}**, like $mapvote, $draft.\n\nWe actualy are working on an elo ranking system 😉\n\nPlease message <@866997795993944084> if you have any suggestions or feedback !")
    await ctx.send(embed=embed)
#$serverinfo
@bot.command(help="Some informations about Civ Private Club !",
        description="SERVERINFO",
        brief="- Informations",
        enabled=True,
        hidden=False)
async def serverinfo(ctx : commands.Context) -> None:
    print(f"\n$serverinfo used by @{ctx.message.author.name} in #{ctx.channel.name}")
    server = ctx.guild
    embed = BotEmbed(title=f"{server.name}", description=f"Are you tired about leavers in Civ 6 Multiplayer ?\nAre you tired about the 3k gametime player bullying you ?\n\nWelcome to the {server.name} !\n\nNo worries, you are at the good place. This discord exists to gather a community of nice peoples who want to play civ, learn civ and discuss about civ !\n\nIf you are new here, don't worry, I'm sure you'll find what you are looking for.")
    embed.add_field(name="Some stats about us :", value =f"Members : **{server.member_count}**\nText Channels : {len(server.text_channels)}\nVoice Channels : {len(server.voice_channels)}", inline=False)
    embed.add_field(name="", value=f"Created by <@866997795993944084> and <@828975075951902733> the {server.created_at.date()}", inline=False)
    await ctx.send(embed=embed)
#$clear X
@bot.command(aliases=['del', 'delete', 'clean'],
        help="Delete the X previous messages in the current Textchannel.",
        description="CLEAR",
        brief="- Clean the channel",
        enabled=True,
        hidden=True)
async def clear(ctx : commands.Context, n : int) -> None:
    print(f"\n$clear {n} used by @{ctx.message.author.name} in #{ctx.channel.name}")
    i : int = 0
    async for message in ctx.channel.history(limit=n+1):
        if (i != 0):
            print(f"  Message deleted from #{ctx.channel.name} ({i}/{n})")
        await message.delete()
        i = i + 1
    print(f"  #{ctx.channel.name} cleaned.")
#$datenow
@bot.command(aliases=['date', 'd'],
        help="Returns the actual date (UTC+1).",
        description="DATENOW",
        brief="- Returns the date",
        enabled=True,
        hidden=False)
async def datenow(ctx : commands.Context) -> None:
    print(f"\n$datenow used by @{ctx.message.author.name} in #{ctx.channel.name}")
    await display_date(ctx)

#$annonce
@bot.command(aliases=['say', 'annonce', 'repeat'],
        help="Tool to make announcements !",
        description="ANNOUNCE",
        brief="- Announce something in a channel",
        enabled=True,
        hidden=True)
async def announce(ctx : commands.Context, channel_ID : int, *, content : str) -> None:
    channel : discord.TextChannel = bot.get_channel(channel_ID)
    await channel.send(content.capitalize())

#$annonce_embed
@bot.command(aliases=['say_embed', 'annonce_embed', 'repeat_embed'],
        help="Tool to make announcements (with embed) !",
        description="ANNOUNCE_EMBED",
        brief="- Announce something in a channel with an embed",
        enabled=True,
        hidden=True)
async def announce_embed(ctx : commands.Context, channel_ID : int, title : str, *, content : str) -> None:
    channel : discord.TextChannel = bot.get_channel(channel_ID)
    embed = BotEmbed(title=title.upper(), description=content.capitalize())
    await channel.send(embed=embed)

#========================================== COMMANDES PRE - GAME ============================================
#$draft 2.0
@bot.command(help="Create randoms list of leaders and assign them to the players.\n\nTake 1 parameter :\n- nb_civs (int) : The number of civs given to each player.\n\nMUST BE USED IN VOICE CHANNEL !\n\nTo use without VoiceChannel, prefer $generic_draft <nb_players> <nb_civs>",
        description="DRAFT",
        brief="- Draw the drafts",
        enabled=True,
        hidden=False)
async def draft(ctx : commands.Context, nb_civs : int) -> None:
    print(f"\n$draft {nb_civs} used by @{ctx.message.author.name} in #{ctx.channel.name}")
    await make_draft(ctx, nb_civs)  
#$blind_draft
@bot.command(help="Create randoms list of leaders and assign them to the players IN PRIVATE MESSAGE.\n\nTake 1 parameter :\n- nb_civs (int) : The number of civs given to each player.\n\nMUST BE USED IN VOICE CHANNEL !",
        description="BLIND_DRAFT",
        brief="- Draw the drafts in private messages",
        enabled=True,
        hidden=False)
async def blind_draft(ctx : commands.Context, nb_civs : int) -> None:
    print(f"\n$blind_draft {nb_civs} used by @{ctx.message.author.name} in #{ctx.channel.name}")
    await make_blind_draft(ctx, nb_civs)
#$draft X Y
@bot.command(help="Create randoms list of leaders and assign them to the players.\n\nTake 2 parameter :\n- nb_players (int) : The number of players in the game.\n- nb_civs (int) : The number of civs given to each player.",
        description="GENERIC_DRAFT",
        brief="- Draw the drafts (for non-VoiceChat use)",
        enabled=True,
        hidden=False)
async def generic_draft(ctx : commands.Context, nb_players : int, nb_civs : int) -> None:
    print(f"\n$generic_draft {nb_players} {nb_civs} used by @{ctx.message.author.name} in #{ctx.channel.name}")
    await make_generic_draft(ctx, nb_players, nb_civs)

#$mapvote v2
@bot.command(help="Launch a mapvote.\n\nBehaves differently if used with or without VoiceChannel.",
        description="MAPVOTE",
        brief="- Launch the mapvote",
        enabled=True,
        hidden=False)
async def mapvote(ctx : commands.Context) -> None:
    print(f"\n$mapvote used by @{ctx.message.author.name} in #{ctx.channel.name}")
    await make_mapvote(ctx)

#========================================== COMMANDES BIRTHDAYS =============================================
#$set_birthday DDMM
@bot.command(help="Set your birthday in the database.\n\nTake 1 parameter :\n- Date (str) : The birthday date to set (Use the following format : DDMM)\nExample : 6th of May -> 0605\nExample : 24th of September -> 2409",
        description="SET_BIRTHDAY",
        brief="- Set your birthday",
        enabled=True,
        hidden=False)
async def set_birthday(ctx : commands.Context, date : str) -> None:
    print(f"\n$set_birthday {date} used by @{ctx.message.author.name} in #{ctx.channel.name}")
    yesno = View()
    yesno.add_item(button_yes)
    yesno.add_item(button_no)
    user = ctx.message.author
    date_parsed = parse_date(date)
    if (date_parsed == "00/00"):
        embed= ErrorEmbed(description="Wrong date format.\nUse the following format : DD/MM.")
        return await ctx.send(embed=embed, delete_after=7)
    if (check_birthday(user)):
        actual_birthday = get_birthday(user)
        if (actual_birthday == date_parsed):
            embed= ErrorEmbed(description=f"Your birthday is already stored in the database at **{actual_birthday}** (DD/MM).")
            return await ctx.send(embed=embed)
        else:
            async def button_yes_callback(interaction : discord.Interaction):
                change_birthday(user, date)
                embed= SuccessEmbed(description=f"Date modified.")
                return await interaction.response.send_message(embed=embed)
            async def button_no_callback(interaction : discord.Interaction):
                embed= ErrorEmbed(title="PROCESS CANCELED", description=f"Date not modified.")
                return await interaction.response.send_message(embed=embed)
            button_yes.callback = button_yes_callback
            button_no.callback = button_no_callback
            embed= BotEmbed(title="Modify birthday ?", description=f"Your birthday is already stored in the database at **{actual_birthday}** (DD/MM).\n\nDo you want to change it for *{date_parsed}* ?")
            return await ctx.send(embed=embed, view=yesno, delete_after=7)
    else:
        async def button_yes_callback(interaction : discord.Interaction):
            add_birthday(user, date)
            embed= SuccessEmbed(description="Birthday added.")
            return await interaction.response.send_message(embed=embed)
        async def button_no_callback(interaction : discord.Interaction):
            embed= ErrorEmbed(title="PROCESS CANCELED", description="Birthday not added.")
            return await interaction.response.send_message(embed=embed)
        button_yes.callback = button_yes_callback
        button_no.callback = button_no_callback
        embed=BotEmbed(title="Add birthday ?", description=f"You birthday is not on the database.\n\nDo you want to set it to *{date_parsed}* ?")
        await ctx.send(embed=embed, view=yesno, delete_after=7)
#$rm_birthday
@bot.command(help="Remove your birthday in the database.",
        description="RM_BIRTHDAY",
        brief="- Remove your birthday",
        enabled=True,
        hidden=False)
async def rm_birthday(ctx : commands.Context) -> None:
    print(f"\n$rm_birthday used by @{ctx.message.author.name} in #{ctx.channel.name}")
    yesno = View()
    yesno.add_item(button_yes)
    yesno.add_item(button_no)
    user = ctx.message.author
    if (check_birthday(user)):
        async def button_yes_callback(interaction : discord.Interaction):
            rem_birthday(user)
            embed= SuccessEmbed(description=f"Birthday deleted from database.")
            return await interaction.response.send_message(embed=embed)
        async def button_no_callback(interaction : discord.Interaction):
            embed= ErrorEmbed(title="PROCESS CANCELED", description=f"Birthday still stored in the database.")
            return await interaction.response.send_message(embed=embed)
        button_yes.callback = button_yes_callback
        button_no.callback = button_no_callback
        embed= BotEmbed(title="Remove birthday ?", description="Do you really want to remove your birthday from the database ?")
        return await ctx.send(embed=embed, view=yesno, delete_after=10)
    else:
        embed= ErrorEmbed(description="No birthday found in the database for you.")
        return await ctx.send(embed=embed)
#$birthdays
@bot.command(help="Display the birthdays in the database.",
        description="BIRTHDAYS",
        brief="- Display the birthdays",
        enabled=True,
        hidden=False)
async def birthdays(ctx : commands.Context) -> None:
    print(f"\n$birthdays used by @{ctx.message.author.name} in #{ctx.channel.name}")
    await display_birthdays(ctx)

#=========================================== COMMANDES RANKED ===============================================
#$report @First @Second @Third ...
@bot.command(help="Report a game in the ranking system.\n\nTake n parameter :\n- User1 (discord.User) : The player won.\n- User2 (discord.User) : The player who finished second.\n...\n- UserN (discord.User) : The player who finished Nth.",
        description="REPORT",
        brief="- Report a game",
        enabled=True,
        hidden=False)
async def report(ctx : commands.Context, *args : discord.User) -> None:
    print(f"\n$report used by @{ctx.message.author.name} in #{ctx.channel.name}")
    users = args
    if (len(users) < 2):
        embed=ErrorEmbed(description="Not enough players in the game reported (minimum 2).")
        return await ctx.send(embed=embed)
    else:
        embed=BotEmbed(title="Verify the Result", description="Please make sure the result reported is correct before verifying it.\nThe report needs to be confirmed by 3 different players (2 for a 1v1).")
        i : int = 0
        message = ""
        while (i < len(users)):
            message = message + f"**{i+1} :** {users[i].mention}\n"
            i = i + 1
        embed.add_field(name="Result reported :", value=message)
        view=ReportView(users)
        await ctx.send(embed=embed, view=view)
#$stats
@bot.command(help="Show your stats (based on reported games).\n\n",
        description="STATS",
        brief="- Show your stats",
        enabled=True,
        hidden=False)
async def stats(ctx : commands.Context) -> None:
    print(f"\n$stats used by @{ctx.message.author.name} in #{ctx.channel.name}")
    user : discord.User = ctx.message.author
    if (not is_player_in_database(user)):
        embed=ErrorEmbed(description=f"{user.mention} not found in the database.\nPlay a game and report the result to create an entry.")
        return await ctx.send(embed=embed)
    elo : int = get_elo(user)
    top1 : int = get_top1(user)
    wins : int = get_wins(user)
    lost : int = get_lost(user)
    date : str = get_date(user)
    rank : int = get_rank(user)
    embed=BotEmbed(title="STATS", description=f"**{user.mention}\nRANK : {rank}**")
    embed.set_thumbnail(url=user.avatar)
    # embed.add_field(name="", value=f"**Games played : {wins+lost}\nElo : {elo}\nTop 1 : {top1}\nWins : {wins}\nLost : {lost}\nLast game played : {date}**")
    embed.add_field(name="", value=f"`Games played    ` : `{wins+lost}`\n`Elo             ` : `{elo}`\n`Top 1           ` : `{top1}`\n`Wins            ` : `{wins}`\n`Lost            ` : `{lost}`\n`Last game played` : `{date}`")
    return await ctx.send(embed=embed)
#$scoreboard
@bot.command(help="Display the leaderboard.",
        description="SCOREBOARD",
        brief="- Display the leaderboard",
        enabled=True,
        hidden=False)
async def leaderboard(ctx : commands.Context) -> None:
    print(f"\n$leaderboard used by @{ctx.message.author.name} in #{ctx.channel.name}")
    await display_scoreboard(ctx)
    return
#$update_leaderboard
@bot.command(help="Refresh the leaderboard in the #leaderboard channel.",
        description="UPDATE_LEADERBOARD",
        brief="- Refresh the leaderboard",
        enabled=True,
        hidden=True)
async def update_leaderboard(ctx : commands.Context) -> None:
    caller : discord.User = ctx.message.author
    if (caller.id != 866997795993944084):
        print(f"\n@{ctx.message.author.name} tried to use $update_leaderboard in #{ctx.channel.name}")
        embed = ErrorEmbed(title="PERMISSIONS ISSUE", description="You're not allowed to use this command.")
        await caller.send(embed=embed)
        return
    else:
        print(f"\n$update_leaderboard used by @{ctx.message.author.name} in #{ctx.channel.name}")
        embed = SuccessEmbed(description="Leaderboard successfuly updated.")
        await ctx.send(embed=embed)
        await update_scoreboard(bot)
        return
#$reset_leaderboard
@bot.command(help="Reset the ranked database.",
        description="RESET_LEADERBOARD",
        brief="- Reset the ranked database",
        enabled=False,
        hidden=True)
async def reset_leaderboard(ctx : commands.Context) -> None:
    caller : discord.User = ctx.message.author
    if (caller.id != 866997795993944084):
        print(f"\n@{ctx.message.author.name} tried to use $clear_leaderboard in #{ctx.channel.name}")
        embed = ErrorEmbed(title="PERMISSIONS ISSUE", description="You're not allowed to use this command.")
        await caller.send(embed=embed)
        return
    else:
        print(f"\n$clear_leaderboard used by @{ctx.message.author.name} in #{ctx.channel.name}")
        if (not is_database_empty()):
            result = rm_all_users()
            if (result):
                embed = SuccessEmbed(description=f"Leaderboard successfully cleared.")
                await update_scoreboard(bot)
            else:
                print("Error during the leaderboard clearing process.")
                embed = ErrorEmbed(description="Error during the leaderboard clearing process.")
        else:
            embed = ErrorEmbed(description="Database is already empty.")
        await ctx.send(embed=embed)
        return
#$add_user
@bot.command(help="Add the user to the database.",
        description="ADD_USER",
        brief="- Add an user",
        enabled=True,
        hidden=True)
async def add_user(ctx : commands.Context, user : discord.User) -> None:
    caller : discord.User = ctx.message.author
    if (caller.id != 866997795993944084):
        print(f"\n@{ctx.message.author.name} tried to use $add_user in #{ctx.channel.name}")
        embed = ErrorEmbed(title="PERMISSIONS ISSUE", description="You're not allowed to use this command.")
        await caller.send(embed=embed)
        return
    else:
        print(f"\n$add_user used by @{ctx.message.author.name} in #{ctx.channel.name}")
        result : int = add_u(user)
        if (result):
            embed = SuccessEmbed(colour=discord.Colour.green(), title="USER ADDED", description=f"{user.mention} successfully added.")
        else:
            embed = ErrorEmbed(description=f"{user.mention} is already in the database.")
        await ctx.send(embed=embed)
        return
#$rm_user
@bot.command(help="Remove the user to the database.",
        description="RM_USER",
        brief="- Remove an user",
        enabled=True,
        hidden=True)
async def rm_user(ctx : commands.Context, user : discord.User) -> None:
    caller : discord.User = ctx.message.author
    if (caller.id != 866997795993944084):
        print(f"\n@{ctx.message.author.name} tried to use $rm_user in #{ctx.channel.name}")
        embed = ErrorEmbed(title="PERMISSIONS ISSUE", description="You're not allowed to use this command.")
        await caller.send(embed=embed)
        return
    else:
        print(f"\n$rm_user used by @{ctx.message.author.name} in #{ctx.channel.name}")
        result : int = rm_u(user)
        if (result):
            embed = SuccessEmbed(description=f"{user.mention} successfully deleted.")
        else:
            embed = ErrorEmbed(description=f"{user.mention} is already not in the database.")
        await ctx.send(embed=embed)
        return

@bot.command(help="Send a formatted lfg message.\n\nTake 0 to 1 parameter :\n- Type of game (Ranked / Casual).",
        description="LFG",
        brief="- Send a formatted lfg message.",
        enabled=True,
        hidden=False)
async def lfg(ctx : commands.Context, format : str = None) -> None:
    print(f"\n$lfg used by @{ctx.message.author.name} in #{ctx.channel.name}")
    if (format == None):
        format=""
    if (format.lower()=="ranked"):
        await ctx.send("<@&1211165398003884093>")
        message=f"Game starting soon !\nClick ✅ if you participate.\nClick ❔ if you're not sure."
        embed=BotEmbed(title="LOOKING FOR GAME", description=message)
        embed.add_field(name="✅ Will play :", value=f"{ctx.message.author.mention}", inline=False)
        embed.add_field(name="❔ Maybe :", value="", inline=False)
        view=LFGView(ctx.message.author)
        await ctx.send(embed=embed, view=view)
        await ctx.send("Hop in https://discord.com/channels/1089289924693459024/1211153791919853579 !")
    elif (format.lower()=="casual"or format.lower()=="chill"):
        await ctx.send("<@&1211165189274337340>")
        message=f"Game starting soon !\nClick ✅ if you participate.\nClick ❔ if you're not sure."
        embed=BotEmbed(title="LOOKING FOR GAME", description=message)
        embed.add_field(name="✅ Will play :", value=f"{ctx.message.author.mention}", inline=False)
        embed.add_field(name="❔ Maybe :", value="", inline=False)
        view=LFGView(ctx.message.author)
        await ctx.send(embed=embed, view=view)
        await ctx.send("Hop in https://discord.com/channels/1089289924693459024/1211153791919853579 !")
    else:
        await ctx.send("<@&1112525992267890780>")
        message=f"Game starting soon !\nClick ✅ if you participate.\nClick ❔ if you're not sure."
        embed=BotEmbed(title="LOOKING FOR GAME", description=message)
        embed.add_field(name="✅ Will play :", value=f"{ctx.message.author.mention}", inline=False)
        embed.add_field(name="❔ Maybe :", value="", inline=False)
        view=LFGView(ctx.message.author)
        await ctx.send(embed=embed, view=view)
        await ctx.send("Hop in https://discord.com/channels/1089289924693459024/1211153791919853579 !")
    return


#=============================================== CHANTIER ===================================================

@bot.command()
async def civilopedia(ctx : commands.Context, article : str = None, lang : str = "en"):
    print(f"$civilopedia used by {ctx.message.author} in {ctx.message.channel}")
    await make_civilopedia(ctx, article, lang)



#================================================== RUN =====================================================
#Run le bot
bot.run(TOKEN)
