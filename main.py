#============================================= INITIALISATION ===============================================

#Import des librairies
import discord
from discord.ext import commands
from discord.ui import Button, View
from birthdays import *
from draft import *
from ranked import *
from classes import Bot, TestButtonView

#Définition du bot
bot = Bot()

#Définition de boutons utiles
button_yes = Button(label="Yes", style=discord.ButtonStyle.green)
button_no = Button(label="No", style=discord.ButtonStyle.red)
button_change = Button(label="Yes", style=discord.ButtonStyle.green)



#============================================ COMMANDES Serveur =============================================

#$hello
@bot.command()
async def hello(ctx : commands.Context):
    server = ctx.guild
    serverName = server.name
    message = f"Hi *Civ enjoyer* ! Let me introduce myself...\nMy name is **Civ Private Bot** (but you can call me CPB), I make my best to add some tools on the **{serverName}**, like map vote, draft (in progress...), ...\nPlease message **@Matezzi** if you have any suggestions to make me more useful !"
    await ctx.send(message)
#$serverinfo
@bot.command()
async def serverinfo(ctx : commands.Context):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"The server **{serverName}** has *{numberOfPerson}* members.\nDescription : {serverDescription}.\nThere are :\n{numberOfTextChannels} channels.\n{numberOfVoiceChannels} voice chats."
    await ctx.send(message)
#$clear X
@bot.command()
async def clear(ctx : commands.Context, nombre:int):
    async for message in ctx.channel.history(limit=nombre+1):
        print(message)
        await message.delete()
#$datenow
@bot.command()
async def datenow(ctx : commands.Context):
    await display_date(ctx)



#============================================   COMMANDES Civ   =============================================

#$draft X Y
@bot.command()
async def draft(ctx : commands.Context, players : int, nb_civs : int):
    await launch_draft(ctx, players, nb_civs)
#$mapvote 2.0
@bot.command()
async def mapvote(ctx : commands.Context):
    embed = CivPrivateBotEmbed(title="MAPVOTE", description="React on the following messages to select the options.")
    embed.add_field(name="MAP", value="🌋 Pangaea **|** 🌊 Seven Seas **|** ⛰️ Highlands **|** 🌄 Rich Highlands **|** 🌍 Continents\n🏝️ Continents and Islands **|** ⛵ Lakes **|** 🐢 Archipelago **|** 🗺️ Terra", inline=False)
    embed.add_field(name="BCY", value="✅ ON **|** ❌ OFF\n⭐ Cap only **|** 🏙️ All cities", inline=False)
    embed.add_field(name="AGE OF THE WORLD", value="🏔️ New **|** 🗻 Standard **|** 🌄 Old", inline=False)
    embed.add_field(name="RIDGE DEFINITION", value="🔴 Standard **|** 🔺 Classic", inline=False)
    embed.add_field(name="RELIGIOUS VICTORY", value="✅ ON **|** ❌ OFF", inline=False)
    embed.add_field(name="BARBARIANS", value="⚔️ Standard **|** 👔 Civilized **|** ❌ OFF", inline=False)
    await ctx.send(embed=embed)
    
    embed=discord.Embed(title="MAP", colour=discord.Colour.light_grey())
    map = await ctx.send(embed=embed)
    await map.add_reaction("🌋")
    await map.add_reaction("🌊")
    await map.add_reaction("⛰️")
    await map.add_reaction("🌄")
    await map.add_reaction("🌍")
    await map.add_reaction("🏝️")
    await map.add_reaction("⛵")
    await map.add_reaction("🐢")
    await map.add_reaction("🗺️")

    embed=discord.Embed(title="BCY", colour=discord.Colour.light_grey())
    bcy = await ctx.send(embed=embed)
    await bcy.add_reaction("✅")
    await bcy.add_reaction("❌")
    await bcy.add_reaction("⭐")
    await bcy.add_reaction("🏙️")

    embed=discord.Embed(title="AGE OF THE WORLD", colour=discord.Colour.light_grey())
    age = await ctx.send(embed=embed)
    await age.add_reaction("🏔️")
    await age.add_reaction("🗻")
    await age.add_reaction("🌄")

    embed=discord.Embed(title="RIDGE", colour=discord.Colour.light_grey())
    ridge = await ctx.send(embed=embed)
    await ridge.add_reaction("🔴")
    await ridge.add_reaction("🔺")

    embed=discord.Embed(title="RELIGIOUS VICTORY", colour=discord.Colour.light_grey())
    religion = await ctx.send(embed=embed)
    await religion.add_reaction("✅")
    await religion.add_reaction("❌")

    embed=discord.Embed(title="BARBARIANS", colour=discord.Colour.light_grey())
    barbs = await ctx.send(embed=embed)
    await barbs.add_reaction("⚔️")
    await barbs.add_reaction("👔")
    await barbs.add_reaction("❌")
    


#=========================================== COMMANDES Birthdays ============================================
    
#$set_birthday DDMM
@bot.command()
async def set_birthday(ctx : commands.Context, date : str):
    yesno = View()
    yesno.add_item(button_yes)
    yesno.add_item(button_no)
    user = ctx.message.author
    date_parsed = parse_date(date)
    if (date_parsed == "00/00"):
        return await ctx.send("Wrong date format.\nUse the following format : DD/MM.", delete_after=7)
    if (check_birthday(user.id)):
        actual_birthday = get_birthday(user.id)
        if (actual_birthday == date_parsed):
            await ctx.send("Your birthday is already stored in the database at **"+actual_birthday+"** (DD/MM).")
        else:
            async def button_yes_callback(interaction):
                change_birthday(user.id, date)
                await interaction.response.send_message("Date modified.")
            async def button_no_callback(interaction):
                await interaction.response.send_message("Date not modified.")
            button_yes.callback = button_yes_callback
            button_no.callback = button_no_callback
            await ctx.send("Your birthday is already stored in the database at **"+actual_birthday+"** (DD/MM).\n\nDo you want to change it for *"+date_parsed+"* ?", view=yesno, delete_after=7)
    else:
        async def button_yes_callback(interaction):
            add_birthday(user.id, date)
            await interaction.response.send_message("Birthday added.")
        async def button_no_callback(interaction):
            await interaction.response.send_message("Birthday not added.")
        button_yes.callback = button_yes_callback
        button_no.callback = button_no_callback
        await ctx.send("You birthday is not on the database.\n\nDo you want to set it to *"+date_parsed+"* ?", view=yesno, delete_after=7)
#$rem_birthday
@bot.command()
async def rm_birthday(ctx : commands.Context):
    yesno = View()
    yesno.add_item(button_yes)
    yesno.add_item(button_no)
    user = ctx.message.author
    if (check_birthday(user.id)):
        async def button_yes_callback(interaction):
            rem_birthday(user.id)
            await interaction.response.send_message("Birthday deleted from database.")
        async def button_no_callback(interaction):
            await interaction.response.send_message("Process aborted.")
        button_yes.callback = button_yes_callback
        button_no.callback = button_no_callback
        await ctx.send("Do you really want to remove your birthday from the database ?", view=yesno, delete_after=10)
    else:
        return await ctx.send("No birthday found in the database for you.")

#$birthdays
@bot.command()
async def birthdays(ctx : commands.Context):
    await display_birthdays(ctx)



#=========================================== COMMANDES DE Ranked ============================================

#$stats
@bot.command()
async def stats(ctx : commands.Context):
    user = ctx.message.author
    await show_stats(ctx, user)
#$report @First @Second @Third ...
@bot.command()
async def report(ctx : commands.Context, *args : discord.User):
    i : int = 0
    players : int = len(args)
    liste_players = []
    while (i < players):
        liste_players.append(args[i])
        i = i + 1
    await build_message(ctx, players, liste_players)
    


#======================================= COMMANDES TESTS & MANAGEMENT =======================================

#$test_button
@bot.command()
async def test_button(ctx : commands.Context):
    return await ctx.send("After 3 clics, this button will be disabled", view=TestButtonView())

#$add_u
@bot.command()
async def add_u(ctx : commands.Context):
    user = ctx.message.author
    await add_user(ctx, user)
#$rem_u
@bot.command()
async def rem_u(ctx : commands.Context):
    user = ctx.message.author
    await remove_user(ctx, user)

#$update_d
@bot.command()
async def update_d(ctx : commands.Context):
    user = ctx.message.author
    await update_date(ctx, user)
#$update_e
@bot.command()
async def update_e(ctx : commands.Context, elo : int):
    user = ctx.message.author
    await update_elo(ctx, user, elo)
#update_l
@bot.command()
async def update_l(ctx : commands.Context):
    user = ctx.message.author
    await update_lost(ctx, user)
#update_t
@bot.command()
async def update_t(ctx : commands.Context):
    user = ctx.message.author
    await update_top1(ctx, user)
#$update_w
@bot.command()
async def update_w(ctx : commands.Context):
    user = ctx.message.author
    await update_win(ctx, user)



#===================================== IN PROGRESS BIRTHDAY AUTOMATION ======================================

# @bot.command()
# async def is_date_stored(ctx : commands.Context, date : str):
#     if (is_in_database(date)):
#         return await ctx.send("This date match with at least 1 birthday stored in the database.")
#     else:
#         return await ctx.send("No birthday stored in the database at this date.")

# @bot.command()
# async def check(ctx : commands.Context):
#     return await (check_today_birthdays(ctx))



#=============================================     LAUNCH      ==============================================

#Run le bot
bot.run("MTExMjcwNTA5Mzk2ODYwMTE5Mg.G5FsiG.kUPa1kBf_K43f9ty9F5PTp4DMc7PPgZ6rc8jUI")