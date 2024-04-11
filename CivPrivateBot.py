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
from draft import *
from mapvote import *
from ranked import *
from civilopedia import *
from feedback import *
from lobby_linker import *
from classes import Bot, BotEmbed, SuccessEmbed, ErrorEmbed, ValidButton, MemberJoinEmbed, InviteEmbed, MemberLeftEmbed, EditedEmbed
from tokens import TOKEN

#Définition du bot
bot = Bot()
#Définition de boutons utiles
button_yes = Button(label="Yes", style=discord.ButtonStyle.green)
button_no = Button(label="No", style=discord.ButtonStyle.red)
button_change = Button(label="Yes", style=discord.ButtonStyle.green)

#=============================================== CONSTANTS ==================================================
welcome_channel_id = 1211150113477627955
feedback_channel_id = 1225240183516172329
suggestion_channel_id = 1225272619192811633
logs_channel_id = 1227074585585913867
WHITE_LIST_CHANNELS_ID = [logs_channel_id, 1211174226346774549, 1211382004260667412, 1225240183516172329, 1225272619192811633, 1211385961330778142, 1211174279220039731, 1211156479269404692, ]
VOICE_CHANNELS_ID = [1211153896857276476, 1211154032366854235, 1211154119000064010, 1211307232952721458]

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
        print(f"  @{interaction.user.name} clicked on the confirm button.")
        #Réagis au clic
        if (interaction.user.id == 866997795993944084): #Si admin
            print(f"    +1 : Admin Access")
            #Remplace par ValidButton
            valid_view = discord.ui.View()
            valid_view.add_item(ValidButton(label="Game reported"))
            await interaction.response.edit_message(view=valid_view)
            await valid_report(bot, self.users) #valid()
            #Message retour
            embed=SuccessEmbed(description="Result confirmed, result stored in the database and player's stats updated.")
            return await interaction.followup.send(embed=embed)
        else: #Si non-admin
            if (is_in_list(interaction.user, self.users)): #Si l'utilisateur était dans la partie
                if (is_in_list(interaction.user, self.users_who_clicked)): #Si l'utilisateur a déjà cliqué
                    print(f"         Already confirmed.") #Console : L'utilisateur a déjà cliqué
                    embed = ErrorEmbed(description="You already confirmed this report.")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                else: #Si l'utilisateur n'a pas encore cliqué
                    self.count = self.count + 1 #+1 clic
                    self.users_who_clicked.append(interaction.user)
                    print(f"    +1 : Confirmed.") #Console : Clic enregistré
                    if (self.count == self.needed_confirm): #Si le nombre de clics est atteint
                        #valid()
                        await valid_report(bot, self.users)
                        #Remplace par ValidButton
                        valid_button : discord.Button = ValidButton()
                        valid_button.label = "✅ Game reported"
                        valid_view = discord.ui.View()
                        valid_view.add_item(valid_button)
                        return await interaction.response.edit_message(view=valid_view)
                    else: #Si le nombre de clics n'est pas atteint
                        #Met à jour le bouton
                        self.label=f"{self.needed_confirm-self.count} more ✅ needed"
                        return await interaction.response.edit_message(view=self.view)
            else: #Si l'utilisateur n'était pas dans la partie
                print(f"         Not in the game.")
                embed = ErrorEmbed(description="You tried to confirm a report which does not concern you.") #Créé le message d'erreur
                await interaction.response.send_message(embed=embed, ephemeral=True) #Envoie un ephemeral d'erreur à l'utilisateur
#View $lfg
class LFGButtonYes(discord.ui.Button):
    def __init__(self, row):
        super().__init__(
            label="✅ Count me in",
            style=discord.ButtonStyle.green,
            row=row
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
    def __init__(self, row):
        super().__init__(
            label="❔ Maybe",
            style=discord.ButtonStyle.grey,
            row=row
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
class LFGButtonStop(discord.ui.Button):
    def __init__(self, author : discord.Member, row : int):
        super().__init__(
            label=f"Delete this post (author only)",
            style=discord.ButtonStyle.red,
            row=row
        )
        self.author : discord.Member = author

    async def callback(self, interaction : discord.Interaction):
        user : discord.Member = interaction.user
        if (user == self.author):
            return await interaction.message.delete()
        else:
            await interaction.response.edit_message(view=self.view)
            embed = ErrorEmbed(title="YOU CAN'T DELETE THIS", description="Only the author of the command can delete this message.")
            return await interaction.followup.send(embed=embed, ephemeral=True)

class LFGButtonJoinChannel(discord.ui.Button):
    def __init__(self, row) -> None:
        super().__init__(
            label="🎤#[LFG] - Looking for Game",
            style=discord.ButtonStyle.blurple,
            row=row,
        )

    async def callback(self, interaction : discord.Interaction):
        return await interaction.response.send_message("Hop in https://discord.com/channels/1089289924693459024/1211153791919853579 !", ephemeral=True)

class LFGView(discord.ui.View):
    def __init__(self, caller : discord.Member) -> None:
        super().__init__(timeout=None)
        self.users : list[discord.User] = []
        self.maybe : list[discord.User] = []
        self.users.append(caller)
        self.add_item(LFGButtonYes(row=0))
        self.add_item(LFGButtonMaybe(row=0))
        self.add_item(LFGButtonJoinChannel(row=1))
        self.add_item(LFGButtonStop(caller, row=2))

#================================================ EVENTS ====================================================

@bot.event #Se déclenche quand le bot est prêt au démarrage
async def on_ready():
    print("         ______  __  __   __       _______  ______    __  __   __  ____   _______  ______       _______   _______  _______")
    print("        / ____/ / / / /  / /      / ___  / / ___  |  / / / /  / / / _  | |__  __/ / ____/      / ___  /  / ___  / /__  __/")
    print("       / /     / / / /  / /      / /__/ / / /__/ /  / / / /  / / / /_| |   / /   / /___       / /__/ /  / /  / /    / /")
    print("      / /     / / | |  / /      / _____/ / ___  /  / / | |  / / / ___  |  / /   / ____/      / ____  | / /  / /    / /")
    print("     / /___  / /  | |_/ /      / /      / /   | | / /  | |_/ / / /  / /  / /   / /___       / /___/ / / /__/ /    / /")
    print("    /_____/ /_/   |____/      /_/      /_/   /_/ /_/   |____/ /_/  /_/  /_/   /_____/      /_______/ /______/    /_/")
    return print(f"\nRock n'Roll !")

@bot.event #Se déclenche quand un nouveau member rejoint le serveur
async def on_member_join(member : discord.Member):
    print(f"New member joined : @{member.name}")
    welcome_channel = bot.get_channel(welcome_channel_id)
    welcome_embed = BotEmbed(title="WELCOME", description=f"Hey guys, {member.mention} just joined the server !")
    welcome_embed.set_thumbnail(url=member.avatar)
    welcome_message = await welcome_channel.send(embed=welcome_embed)
    await welcome_message.add_reaction("👋")
    log_channel = bot.get_channel(logs_channel_id)
    log_embed = MemberJoinEmbed(description=f"{member.mention} joined the server !")
    log_embed.set_thumbnail(url=member.avatar)
    log_embed.add_field(name=f"Name :", value=f"**{member.name}**", inline=False)
    log_embed.add_field(name=f"ID :", value=f"{member.id}", inline=False)
    log_embed.add_field(name=f"Joined :", value=f"{datetime.datetime.now().date()} at {datetime.datetime.now().time()}", inline=False)
    log_embed.add_field(name=f"Account created :", value=f"{member.created_at.date()}", inline=False)
    return await log_channel.send(embed=log_embed)

@bot.event #Se déclenche quand un membre quitte le serveur
async def on_member_remove(member : discord.Member):
    print(f"Member left... @{member.name}")
    log_channel = bot.get_channel(logs_channel_id)
    log_embed = MemberLeftEmbed(description=f"{member.mention} just left...")
    log_embed.set_thumbnail(url=member.avatar)
    log_embed.add_field(name=f"Left :", value=f"{datetime.datetime.now().date()} at {datetime.datetime.now().time()}", inline=False)
    return await log_channel.send(embed=log_embed)

@bot.event #Se déclenche lorsqu'un membre crée une nouvelle invitation
async def on_invite_create(invite : discord.Invite):
    print(f"\nNew Invite created by {invite.inviter} : {invite.code}")
    description : str = f"New Invite created by : **{invite.inviter.mention}** at {datetime.datetime.now()}."
    embed = InviteEmbed(description=description)
    embed.set_thumbnail(url=invite.inviter.avatar)
    channel = bot.get_channel(logs_channel_id)
    return await channel.send(embed=embed)

@bot.event #Se déclenche lorsqu'un message est supprimé
async def on_message_delete(message : discord.Message):
    if (not message.channel.id in WHITE_LIST_CHANNELS_ID):
        print(f"A message from @{message.author.name} was deleted in #{message.channel.name}.")
        embed = ErrorEmbed(title="MESSAGE DELETED", description=f"A message from **{message.author.mention}** was deleted in **#{message.channel.name}**.")
        embed.set_thumbnail(url=message.author.avatar)
        embed.add_field(name="Content :", value=f"{message.content}", inline=False)
        channel = bot.get_channel(logs_channel_id)
        await channel.send(embed=embed)
    return

@bot.event #Se déclenche lorsqu'un message est édité
async def on_message_edit(before : discord.Message, after : discord.Message):
    if ((not before.channel.id in WHITE_LIST_CHANNELS_ID) and (before.author.id != bot.user.id)):
        print(f"A message from @{before.author.name} was edited in #{before.channel.name}.")
        embed = EditedEmbed(description=f"A message from {before.author.mention} was edited in **#{before.channel.name}**.")
        embed.set_thumbnail(url=before.author.avatar)
        embed.add_field(name="**Before :**", value=f"{before.content}", inline=False)
        embed.add_field(name="**After :**", value=f"{after.content}", inline=False)
        channel = bot.get_channel(logs_channel_id)
        await channel.send(embed=embed)
    return

@bot.event
async def on_command_error(ctx : commands.Context, error):
    if isinstance(error, commands.CommandNotFound):
        embed = ErrorEmbed(title="UNKNOWN COMMAND", description="This commands is not recognized by the bot. Check https://discord.com/channels/1089289924693459024/1211159694115348530/1211161705128665169 or use ***$help*** to see the list of the commands supported.")
        await ctx.send(embed=embed)

#============================================ COMMANDES INFOS ===============================================
#$ping
@bot.command(aliases=['p', 'pong'],
        help="Respond PONG if the bot is running.",
        description="PING",
        brief="- Pong",
        enabled=True,
        hidden=False)
async def ping(ctx : commands.Context) -> None:
    print(f"$ping used by @{ctx.message.author.name} in #{ctx.channel.name}")
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
    print(f"$hello used by @{ctx.message.author.name} in #{ctx.channel.name}")
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
    print(f"$serverinfo used by @{ctx.message.author.name} in #{ctx.channel.name}")
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
    print(f"$clear {n} used by @{ctx.message.author.name} in #{ctx.channel.name}")
    i : int = 0
    async for message in ctx.channel.history(limit=n+1):
        await message.delete()
        if (i != 0):
            print(f"  Message deleted from #{ctx.channel.name} ({i}/{n})")
        i = i + 1
    print(f"  #{ctx.channel.name} cleaned.")

#========================================== COMMANDES PRE - GAME ============================================
#$lfg
@bot.command(help="Send a formatted lfg message.\n\nTake 0 to 1 parameter :\n- Type of game (Ranked / Casual).",
        description="LFG",
        brief="- Send a formatted lfg message.",
        enabled=True,
        hidden=False)
async def lfg(ctx : commands.Context, format : str = None) -> None:
    print(f"$lfg used by @{ctx.message.author.name} in #{ctx.channel.name}")
    if (format == None):
        format=""
    if (format.lower()=="ranked"):
        message=f"Game starting soon !\nClick ✅ if you participate.\nClick ❔ if you're not sure."
        embed=BotEmbed(title="LOOKING FOR GAME", description=message)
        embed.add_field(name="✅ Will play :", value=f"{ctx.message.author.mention}", inline=False)
        embed.add_field(name="❔ Maybe :", value="", inline=False)
        view=LFGView(ctx.message.author)
        await ctx.send("<@&1211165398003884093>", embed=embed, view=view)
    elif (format.lower()=="casual"or format.lower()=="chill"):
        message=f"Game starting soon !\nClick ✅ if you participate.\nClick ❔ if you're not sure."
        embed=BotEmbed(title="LOOKING FOR GAME", description=message)
        embed.add_field(name="✅ Will play :", value=f"{ctx.message.author.mention}", inline=False)
        embed.add_field(name="❔ Maybe :", value="", inline=False)
        view=LFGView(ctx.message.author)
        await ctx.send("<@&1211165189274337340>", embed=embed, view=view)
    else:
        message=f"Game starting soon !\nClick ✅ if you participate.\nClick ❔ if you're not sure."
        embed=BotEmbed(title="LOOKING FOR GAME", description=message)
        embed.add_field(name="✅ Will play :", value=f"{ctx.message.author.mention}", inline=False)
        embed.add_field(name="❔ Maybe :", value="", inline=False)
        view=LFGView(ctx.message.author)
        await ctx.send("<@&1112525992267890780>", embed=embed, view=view)
    return
#$draft 2.0
@bot.command(help="Create randoms list of leaders and assign them to the players.\n\nTake 1 parameter :\n- nb_civs (int) : The number of civs given to each player.\n\nMUST BE USED IN VOICE CHANNEL !\n\nTo use without VoiceChannel, prefer $generic_draft <nb_players> <nb_civs>",
        description="DRAFT",
        brief="- Draw the drafts",
        enabled=True,
        hidden=False)
async def draft(ctx : commands.Context, nb_civs : int) -> None:
    print(f"$draft {nb_civs} used by @{ctx.message.author.name} in #{ctx.channel.name}")
    await make_draft(ctx, nb_civs)  
#$blind_draft
@bot.command(help="Create randoms list of leaders and assign them to the players IN PRIVATE MESSAGE.\n\nTake 1 parameter :\n- nb_civs (int) : The number of civs given to each player.\n\nMUST BE USED IN VOICE CHANNEL !",
        description="BLIND_DRAFT",
        brief="- Draw the drafts in private messages",
        enabled=True,
        hidden=False)
async def blind_draft(ctx : commands.Context, nb_civs : int) -> None:
    print(f"$blind_draft {nb_civs} used by @{ctx.message.author.name} in #{ctx.channel.name}")
    await make_blind_draft(ctx, nb_civs)
#$draft X Y
@bot.command(help="Create randoms list of leaders and assign them to the players.\n\nTake 2 parameter :\n- nb_players (int) : The number of players in the game.\n- nb_civs (int) : The number of civs given to each player.",
        description="GENERIC_DRAFT",
        brief="- Draw the drafts (for non-VoiceChat use)",
        enabled=True,
        hidden=False)
async def generic_draft(ctx : commands.Context, nb_players : int, nb_civs : int) -> None:
    print(f"$generic_draft {nb_players} {nb_civs} used by @{ctx.message.author.name} in #{ctx.channel.name}")
    await make_generic_draft(ctx, nb_players, nb_civs)

#$mapvote
@bot.command(help="Launch a mapvote.",
        description="MAPVOTE",
        brief="- Launch the mapvote",
        enabled=True,
        hidden=False)
async def mapvote(ctx : commands.Context) -> None:
    print(f"$mapvote used by @{ctx.message.author.name} in #{ctx.channel.name}")
    voice_channel = None
    for channel_id in VOICE_CHANNELS_ID:
        channel : discord.VoiceChannel = bot.get_channel(channel_id)
        nb_users = len(channel.members)
        if ((nb_users == 0) and (channel.user_limit > 2) and (voice_channel == None)):
            voice_channel = channel
    if (voice_channel == None):
        category = discord.utils.utils.get(ctx.guild().categories, id=1211152499772227697)
        nb_voice_channel = len(category.voice_channels)
        voice_channel = await category.create_voice_channel(name=f"War Room #{nb_voice_channel-1}", position=nb_voice_channel-1, user_limit=10)

    await make_mapvote(ctx, voice_channel)

#$longer_mapvote
@bot.command(help="Launch a longer mapvote than $mapvote.",
        description="LONGER_MAPVOTE",
        brief="- Launch a longer mapvote",
        enabled=True,
        hidden=False)
async def longer_mapvote(ctx : commands.Context) -> None:
    print(f"$longer_mapvote used by @{ctx.message.author.name} in #{ctx.channel.name}")
    voice_channel = None
    for channel_id in VOICE_CHANNELS_ID:
        channel : discord.VoiceChannel = bot.get_channel(channel_id)
        nb_users = len(channel.members)
        if ((nb_users == 0) and (channel.user_limit > 2) and (voice_channel == None)):
            voice_channel = channel
    if (voice_channel == None):
        category = discord.utils.utils.get(ctx.guild().categories, id=1211152499772227697)
        nb_voice_channel = len(category.voice_channels)
        voice_channel = await category.create_voice_channel(name=f"War Room #{nb_voice_channel-1}", position=nb_voice_channel-1, user_limit=10)
    await make_longer_mapvote(ctx, voice_channel)

#=========================================== COMMANDES RANKED ===============================================
#$report @First @Second @Third ...
@bot.command(help="Report a game in the ranking system.\n\nTake n parameter :\n- User1 (discord.User) : The player won.\n- User2 (discord.User) : The player who finished second.\n...\n- UserN (discord.User) : The player who finished Nth.",
        description="REPORT",
        brief="- Report a game",
        enabled=True,
        hidden=False)
async def report(ctx : commands.Context, *args : discord.User) -> None:
    print(f"$report used by @{ctx.message.author.name} in #{ctx.channel.name}")
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
    print(f"$stats used by @{ctx.message.author.name} in #{ctx.channel.name}")
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
    print(f"$leaderboard used by @{ctx.message.author.name} in #{ctx.channel.name}")
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
        print(f"@{ctx.message.author.name} tried to use $update_leaderboard in #{ctx.channel.name}")
        embed = ErrorEmbed(title="PERMISSIONS ISSUE", description="You're not allowed to use this command.")
        await caller.send(embed=embed)
        return
    else:
        print(f"$update_leaderboard used by @{ctx.message.author.name} in #{ctx.channel.name}")
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
        print(f"@{ctx.message.author.name} tried to use $clear_leaderboard in #{ctx.channel.name}")
        embed = ErrorEmbed(title="PERMISSIONS ISSUE", description="You're not allowed to use this command.")
        await caller.send(embed=embed)
        return
    else:
        print(f"$clear_leaderboard used by @{ctx.message.author.name} in #{ctx.channel.name}")
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
        print(f"@{ctx.message.author.name} tried to use $add_user in #{ctx.channel.name}")
        embed = ErrorEmbed(title="PERMISSIONS ISSUE", description="You're not allowed to use this command.")
        await caller.send(embed=embed)
        return
    else:
        print(f"$add_user used by @{ctx.message.author.name} in #{ctx.channel.name}")
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
        print(f"@{ctx.message.author.name} tried to use $rm_user in #{ctx.channel.name}")
        embed = ErrorEmbed(title="PERMISSIONS ISSUE", description="You're not allowed to use this command.")
        await caller.send(embed=embed)
        return
    else:
        print(f"$rm_user used by @{ctx.message.author.name} in #{ctx.channel.name}")
        result : int = rm_u(user)
        if (result):
            embed = SuccessEmbed(description=f"{user.mention} successfully deleted.")
        else:
            embed = ErrorEmbed(description=f"{user.mention} is already not in the database.")
        await ctx.send(embed=embed)
        return


#============================================== CIVILOPEDIA =================================================

@bot.command(help="Open the civilopedia.",
        description="CIVILOPEDIA",
        brief="- open the Civilopedia",
        enabled=True,
        hidden=False)
async def civilopedia(ctx : commands.Context, article : str = None, lang : str = "en"):
    print(f"$civilopedia used by {ctx.message.author} in {ctx.message.channel}")
    await make_civilopedia(ctx, article, lang)

#=========================================== FEEDBACKS & IDEAS ==============================================

@bot.command(help="Send a suggestion to make this server better.",
        description="MAKE_SUGGESTION",
        brief="- make a suggestion",
        enabled=True,
        hidden=False)
async def make_suggestion(ctx : commands.Context):
    print(f"$make_suggestion used by {ctx.message.author} in {ctx.message.channel}")
    channel_suggestion = bot.get_channel(suggestion_channel_id)
    await create_suggestion(ctx, channel_suggestion)

@bot.command(help="Send a feedback about your experience on this community.",
        description="FEEDBACK",
        brief="- Send a feedback",
        enabled=True,
        hidden=False)
async def feedback(ctx : commands.Context):
    print(f"$feedback used by {ctx.message.author} in {ctx.message.channel}")
    channel_feedback = bot.get_channel(feedback_channel_id)
    await make_feedback(ctx, channel_feedback)

#================================================= STEAM ====================================================

@bot.command(help="Link/Modify/Delete a Steam profile to enable the $lobby command.",
        description="SET_STEAM",
        brief="- Link your steam profile",
        enabled=True,
        hidden=False)
async def set_steam(ctx : commands.Context):
    print(f"$set_steam used by {ctx.message.author} in {ctx.message.channel}")
    await link_steam_account(ctx)

@bot.command(help="Display a link to your lobby.\nOnly works for Steam users.\n\nYou have to link your Steam Profile first by using $set_steam.",
        description="LOBBY",
        brief="- Display a link to your active lobby (Steam)",
        enabled=True,
        hidden=False)
async def lobby(ctx : commands.Context):
    print(f"$lobby used by {ctx.message.author} in {ctx.message.channel}")
    await display_lobby_link(ctx)

#================================================== RUN =====================================================
#Run le bot
bot.run(TOKEN)
