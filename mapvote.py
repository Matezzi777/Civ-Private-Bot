import discord
from discord.ext import commands
from classes import CivPrivateBotEmbed

async def make_mapvote(ctx : commands.Context) -> None:
    author = ctx.message.author
    
    if (author.voice):
        channel = author.voice.channel
        users = channel.members
        message = ""
        i : int = 0
        while (i < len(users)):
            message = message + f"{users[i].mention} "
            i = i + 1
        await ctx.send(message)

    embed = CivPrivateBotEmbed(title="MAPVOTE", description=f"\nReact on the following messages to select the options.")
    embed.add_field(name="MAP", value="🌋 Pangaea **|** 🌊 Seven Seas **|** ⛰️ Highlands **|** 🌄 Rich Highlands **|** 🌍 Continents\n🏝️ Continents and Islands **|** ⛵ Lakes **|** 🐢 Archipelago **|** 🗺️ Terra", inline=False)
    embed.add_field(name="BCY", value="✅ ON **|** ❌ OFF\n⭐ Cap only **|** 🏙️ All cities", inline=False)
    embed.add_field(name="AGE OF THE WORLD", value="🏔️ New **|** 🗻 Standard **|** 🌄 Old", inline=False)
    embed.add_field(name="RIDGE DEFINITION", value="🔴 Standard **|** 🔺 Classic", inline=False)
    embed.add_field(name="RELIGIOUS VICTORY", value="✅ ON **|** ❌ OFF", inline=False)
    embed.add_field(name="BARBARIANS", value="⚔️ Standard **|** 👔 Civilized **|** ❌ OFF", inline=False)
    await ctx.send(embed=embed)
    
    map = await ctx.send("**MAP**")
    await map.add_reaction("🌋")
    await map.add_reaction("🌊")
    await map.add_reaction("⛰️")
    await map.add_reaction("🌄")
    await map.add_reaction("🌍")
    await map.add_reaction("🏝️")
    await map.add_reaction("⛵")
    await map.add_reaction("🐢")
    await map.add_reaction("🗺️")

    bcy = await ctx.send("**BCY**")
    await bcy.add_reaction("✅")
    await bcy.add_reaction("❌")
    await bcy.add_reaction("⭐")
    await bcy.add_reaction("🏙️")

    age = await ctx.send("**AGE OF THE WORLD**")
    await age.add_reaction("🏔️")
    await age.add_reaction("🗻")
    await age.add_reaction("🌄")

    ridge = await ctx.send("**RIDGE DEFINITION**")
    await ridge.add_reaction("🔴")
    await ridge.add_reaction("🔺")

    religion = await ctx.send("**RELIGIOUS VICTORY**")
    await religion.add_reaction("✅")
    await religion.add_reaction("❌")

    barbs = await ctx.send("**BARBARIANS**")
    await barbs.add_reaction("⚔️")
    await barbs.add_reaction("👔")
    await barbs.add_reaction("❌")

async def make_mapvote_v2(ctx : commands.Context) -> None:
    author = ctx.message.author
    
    if (not author.voice):
        embed=CivPrivateBotEmbed(title="🎤 JOIN A VOICE CHANNEL 🎤", description="Please, join a voice channel with the other players to use this command.\nIf you can't use the voice chat, consider using *$generic_draft* instead.")
        await ctx.send(embed=embed)
        return
    else:
        channel = author.voice.channel
        users = channel.members
        nb_users : int = len(users)
        message = ""
        i : int = 0
        while (i < nb_users):
            message = message + f"{users[i].mention} "
            i = i + 1
        await ctx.send(message)
    
    if (nb_users < 2):
        embed = CivPrivateBotEmbed(title="PROCESS ABORTED", description="It looks like you are alone here, find peoples to play with before to use this command.", color=discord.Colour.red())
        await ctx.send(embed=embed)
    else:
        embed = CivPrivateBotEmbed(title="MAPVOTE", description=f"\nReact on the following messages to select the options.")
        embed.add_field(name="MAP", value="🌋 Pangaea **|** 🌊 Seven Seas **|** ⛰️ Highlands **|** 🌄 Rich Highlands **|** 🌍 Continents\n🏝️ Continents and Islands **|** ⛵ Lakes **|** 🐢 Archipelago **|** 🗺️ Terra", inline=False)
        embed.add_field(name="BCY", value="✅ ON **|** ❌ OFF\n⭐ Cap only **|** 🏙️ All cities", inline=False)
        embed.add_field(name="AGE OF THE WORLD", value="🏔️ New **|** 🗻 Standard **|** 🌄 Old", inline=False)
        embed.add_field(name="RIDGE DEFINITION", value="🔴 Standard **|** 🔺 Classic", inline=False)
        embed.add_field(name="RELIGIOUS VICTORY", value="✅ ON **|** ❌ OFF", inline=False)
        embed.add_field(name="BARBARIANS", value="⚔️ Standard **|** 👔 Civilized **|** ❌ OFF", inline=False)
        await ctx.send(embed=embed)

        map = await ctx.send("**MAP**")
        await map.add_reaction("🌋")
        await map.add_reaction("🌊")
        await map.add_reaction("⛰️")
        await map.add_reaction("🌄")
        await map.add_reaction("🌍")
        await map.add_reaction("🏝️")
        await map.add_reaction("⛵")
        await map.add_reaction("🐢")
        await map.add_reaction("🗺️")

        bcy = await ctx.send("**BCY**")
        await bcy.add_reaction("✅")
        await bcy.add_reaction("❌")
        await bcy.add_reaction("⭐")
        await bcy.add_reaction("🏙️")

        age = await ctx.send("**AGE OF THE WORLD**")
        await age.add_reaction("🏔️")
        await age.add_reaction("🗻")
        await age.add_reaction("🌄")

        ridge = await ctx.send("**RIDGE DEFINITION**")
        await ridge.add_reaction("🔴")
        await ridge.add_reaction("🔺")

        religion = await ctx.send("**RELIGIOUS VICTORY**")
        await religion.add_reaction("✅")
        await religion.add_reaction("❌")

        barbs = await ctx.send("**BARBARIANS**")
        await barbs.add_reaction("⚔️")
        await barbs.add_reaction("👔")
        await barbs.add_reaction("❌")