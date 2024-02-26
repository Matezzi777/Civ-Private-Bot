#============================================= INITIALISATION ===============================================
#Import des modules
import discord
from discord.ext import commands

bot_version : str = "Civ Private Bot 2.1"

#================================================== BOT =====================================================
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=discord.Intents.all(), description="Civ Private Bot v2.1")

    async def setup_hook(self):
        await self.tree.sync()
    
    async def on_ready(self):
        print(f"{self.user.id} successfully logged in as {self.user.name}.\nRock n'Roll !")

#================================================= EMBEDS ===================================================
class BotEmbed(discord.Embed):
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
        self.set_footer(text=bot_version)

class SuccessEmbed(discord.Embed):
    def __init__(self, *, colour=discord.Colour.green(), color=discord.Colour.green(), title="SUCCESS", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
            )
        self.set_footer(text=bot_version)

class ErrorEmbed(discord.Embed):
    def __init__(self, *, colour=discord.Colour.red(), color=discord.Colour.red(), title="ERROR", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
            )
        self.set_footer(text=bot_version)

# BUTTONS
#Bouton choix validé générique
class ValidButton(discord.ui.Button):
    def __init__(self) -> None:
        super().__init__(
            label=" - ",
            style=discord.ButtonStyle.green
        )
    
    async def callback(self, interaction : discord.Interaction):
        await interaction.response.edit_message(view=self.view)