import discord
from discord.ext import commands



##################################################   BOT   ##################################################

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=discord.Intents.all(), description="This bot is being actively developped by @Matezzi.")

    async def setup_hook(self):
        await self.tree.sync()
    
    async def on_ready(self):
        print(f"{self.user.id} successfully logged in as {self.user.name}.\nRock n'Roll !")



##################################################  EMBEDS  #################################################

class CivPrivateBotEmbed(discord.Embed):
    def __init__(self, *, colour=discord.Colour.purple(), color=discord.Colour.purple(), title=None, type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
            )
        self.set_footer(text="Civ Private Bot 2.0")



################################################## BUTTONS ##################################################

class ButtonTest(discord.ui.Button):
    def __init__(self) -> None:
        super().__init__(
            label="Click Me !",
            style=discord.ButtonStyle.green
        )
        self.count = 0

    async def callback(self, interaction : discord.Interaction) -> None:
        self.count = self.count + 1

        if self.count >= 3:
            self.label="Disabled"
            self.disabled=True
        else:
            self.label=f"{self.count} clic"
        await interaction.response.edit_message(view=self.view)
        await interaction.followup.send("Oh yeah ! Keep clicking !!!")



##################################################   VIEWS   #################################################

class TestButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(ButtonTest())