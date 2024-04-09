#============================================= INITIALISATION ===============================================
#Import des modules
import discord
from discord.ext import commands

#=============================================== CONSTANTS ==================================================
VERSION = "2.4"
BOT_EMBED_RGB = discord.Colour.from_rgb(118, 22, 148)
SUCCESS_RGB = discord.Colour.from_rgb(14, 209, 96)
ERROR_RGB = discord.Colour.from_rgb(204, 30, 15)
FEEDBACK_RGB = discord.Colour.from_rgb(84, 5, 241)
SUGGESTION_RGB = discord.Colour.from_rgb(168, 67, 0)
STEAM_RGB = discord.Colour.from_rgb(18, 48, 100)
JOIN_RGB = discord.Colour.from_rgb(184, 233, 134)
LEFT_RGB = discord.Colour.from_rgb(255, 246, 175)
INVITE_RGB = discord.Colour.from_rgb(14, 102, 201)
EDIT_RGB = discord.Colour.from_rgb(14, 102, 201)

#================================================= TASKS ====================================================

#================================================== BOT =====================================================
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=discord.Intents.all(), description=f"Civ Private Bot v{VERSION}")

    async def setup_hook(self):
        await self.tree.sync()

#================================================= EMBEDS ===================================================
class BotEmbed(discord.Embed):
    def __init__(self, *, colour=BOT_EMBED_RGB, color=BOT_EMBED_RGB, title=None, type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
            )
        self.set_footer(text=f"Civ Private Bot {VERSION}")
class SuccessEmbed(discord.Embed):
    def __init__(self, *, colour=SUCCESS_RGB, color=SUCCESS_RGB, title="SUCCESS", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
            )
        self.set_footer(text=f"Civ Private Bot {VERSION}")
class ErrorEmbed(discord.Embed):
    def __init__(self, *, colour=ERROR_RGB, color=ERROR_RGB, title="ERROR", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
            )
        self.set_footer(text=f"Civ Private Bot {VERSION}")
class FeedbackEmbed(discord.Embed):
    def __init__(self, *, colour=FEEDBACK_RGB, color=FEEDBACK_RGB, title="NEW FEEDBACK !", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
        )
        self.set_footer(text=f"Civ Private Bot {VERSION}")
class SuggestionEmbed(discord.Embed):
    def __init__(self, *, colour=SUGGESTION_RGB, color=SUGGESTION_RGB, title="NEW SUGGESTION !", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
        )
        self.set_footer(text=f"Civ Private Bot {VERSION}")
class SteamEmbed(discord.Embed):
    def __init__(self, *, colour=STEAM_RGB, color=STEAM_RGB, title="LINK YOUR ACCOUNT", type='rich', url=None, description="Click 🔗 to link your Steam account", timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
        )
        self.set_footer(text=f"Civ Private Bot {VERSION}")
class MemberJoinEmbed(discord.Embed):
    def __init__(self, *, colour=JOIN_RGB, color=JOIN_RGB, title="NEW MEMBER JOINED", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
        )
        self.set_footer(text=f"Civ Private Bot {VERSION}")
class MemberLeftEmbed(discord.Embed):
    def __init__(self, *, colour=LEFT_RGB, color=LEFT_RGB, title="MEMBER LEFT", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
        )
        self.set_footer(text=f"Civ Private Bot {VERSION}")
class InviteEmbed(discord.Embed):
    def __init__(self, *, colour=INVITE_RGB, color=INVITE_RGB, title="NEW INVITE CREATED", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
        )
        self.set_footer(text=f"Civ Private Bot {VERSION}")
class EditedEmbed(discord.Embed):
    def __init__(self, *, colour=EDIT_RGB, color=EDIT_RGB, title="MESSAGE EDITED", type='rich', url=None, description=None, timestamp=None) -> None:
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp
        )
        self.set_footer(text=f"Civ Private Bot {VERSION}")

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