################################################## INITIALISATION ##################################################

#import des librairies
import discord
from discord.ext import commands
from discord.ui import Button, View
from birthdays import *

#définition du bot (prefix, accès, description)
bot = commands.Bot(command_prefix="$",intents=discord.Intents.all(),description="$mapvote or $serverinfo.")

#définition de boutons utiles
button_yes = Button(label="Yes", style=discord.ButtonStyle.green)
button_change = Button(label="Yes", style=discord.ButtonStyle.green)
button_no = Button(label="No", style=discord.ButtonStyle.red)

#envoie de "Ready !" dans la console quand le bot est en ligne
@bot.event
async def on_ready():
    print("Ready !")



##################################################    COMMANDES   ##################################################


#commande $hello
@bot.command()
async def hello(ctx : commands.Context):
    server = ctx.guild
    serverName = server.name
    message = f"Hi *Civ enjoyer* ! Let me introduce myself...\nMy name is **Civ Private Bot** (but you can call me CPB), I make my best to add some tools on the **{serverName}**, like map vote, draft (in progress...), ...\nPlease message **@Matezzi** if you have any suggestions to make me more useful !"
    await ctx.send(message)

#commande $serverinfo
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

#commande clear
@bot.command()
async def clear(ctx : commands.Context, nombre:int):
    async for message in ctx.channel.history(limit=nombre+1):
        print(message)
        await message.delete()

#commande draft
@bot.command()
async def mapvote(ctx : commands.Context):
    #map
    map = await ctx.send("## Map :\n🌋 Pangaea | 🌊 Seven Seas | ⛰️ Highlands | 🌄 Rich Highlands | 🌍 Continents\n🏝️ Continents and Islands | ⛵ Lakes | 🐢 Archipelago | 🗺️ Terra")
    await map.add_reaction("🌋")
    await map.add_reaction("🌊")
    await map.add_reaction("⛰️")
    await map.add_reaction("🌄")
    await map.add_reaction("🌍")
    await map.add_reaction("🏝️")
    await map.add_reaction("⛵")
    await map.add_reaction("🐢")
    await map.add_reaction("🗺️")

    #BCY
    bcy = await ctx.send("## BCY :\n✅ ON | ❌ OFF\n⭐ Cap only | 🏙️ All cities")
    await bcy.add_reaction("✅")
    await bcy.add_reaction("❌")
    await bcy.add_reaction("⭐")
    await bcy.add_reaction("🏙️")

    #age du monde
    age = await ctx.send("## Age of the world :\n🏔️ New | 🗻 Standard | 🌄 Old")
    await age.add_reaction("🏔️")
    await age.add_reaction("🗻")
    await age.add_reaction("🌄")

    #ridge
    ridge = await ctx.send("## Ridge Definition :\n🔴 Standard | 🔺 Classic")
    await ridge.add_reaction("🔴")
    await ridge.add_reaction("🔺")

    #religieuse
    religion = await ctx.send("## Religion Victory :\n✅ ON | ❌ OFF")
    await religion.add_reaction("✅")
    await religion.add_reaction("❌")

    #barbares
    barbs = await ctx.send("## Barbarian Tribes :\n⚔️ Standard | 👔 Civilized | ❌ OFF")
    await barbs.add_reaction("⚔️")
    await barbs.add_reaction("👔")
    await barbs.add_reaction("❌")

#commande set_birthday
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

#commande birthdays
@bot.command()
async def birthdays(ctx : commands.Context):
    await display_birthdays(ctx)
    


##################################################     LAUNCH     ##################################################


#Run le bot
bot.run(TOKEN)
