import discord
import discord.ui
from discord.ext import commands
from classes import BotEmbed, SuccessEmbed, FeedbackEmbed, SuggestionEmbed

#================================================================= SUGGESTION =================================================================

class ButtonStartSuggestion(discord.ui.Button):
    def __init__(self, channel : discord.TextChannel):
        super().__init__(
            label="✅ Give my suggestion!",
            style=discord.ButtonStyle.green)
        self.channel : discord.TextChannel = channel
    
    async def callback(self, interaction : discord.Interaction):
        await interaction.response.send_modal(SuggestionModal(self.channel))
class SuggestionView(discord.ui.View):
    def __init__(self, channel)-> None:
        super().__init__()
        self.add_item(ButtonStartSuggestion(channel))
class SuggestionModal(discord.ui.Modal):
    def __init__(self, channel : discord.TextChannel) -> None:
        super().__init__(title="GIVE A SUGGESTION !")
        self.add_item(discord.ui.InputText(label="NAME", style=discord.InputTextStyle.short, placeholder="Name your suggestion !", min_length=5, max_length=50, required=True))
        self.add_item(discord.ui.InputText(label="DESCRIPTION", style=discord.InputTextStyle.long, placeholder="Tell me more about the details of your idea...", min_length=20, max_length=None, required=True))
        self.channel : discord.TextChannel = channel

    async def callback(self, interaction : discord.Interaction):
        name = self.children[0].value
        description = self.children[1].value
        embed = SuccessEmbed(title="SUGGESTION SENT", description="Thanks for your suggestion!")
        await process_suggestion(self.channel, name, description)
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def create_suggestion(ctx : commands.Context, channel):
    embed = BotEmbed(title="NEW SUGGESTION", description="Click ✅ to give your suggestion!")
    await ctx.send(embed=embed, view=SuggestionView(channel))
async def process_suggestion(channel : discord.TextChannel, name, description):
    embed = SuggestionEmbed()
    embed.add_field(name=f"**{name}**", value=description, inline=False)
    print(f"  Suggestion sent !")
    await channel.send(embed=embed)

#================================================================= FEEDBACK ==================================================================

class ButtonStartFeedback(discord.ui.Button):
    def __init__(self, channel : discord.TextChannel):
        super().__init__(
            label="✅ Start the feedback!",
            style=discord.ButtonStyle.green)
        self.channel : discord.TextChannel = channel
    
    async def callback(self, interaction : discord.Interaction):
        await interaction.response.send_modal(FeedbackModal(self.channel))
class FeedbackView(discord.ui.View):
    def __init__(self, channel)-> None:
        super().__init__()
        self.add_item(ButtonStartFeedback(channel))
class FeedbackModal(discord.ui.Modal):
    def __init__(self, channel : discord.TextChannel) -> None:
        super().__init__(title="GIVE YOUR FEEDBACK !")
        self.add_item(discord.ui.InputText(label="RATE YOUR EXPERIENCE ON THE SERVER", style=discord.InputTextStyle.short, placeholder="... / 5", min_length=1, max_length=1, required=True))
        self.add_item(discord.ui.InputText(label="DESCRIPTION", style=discord.InputTextStyle.long, placeholder="Give your feedback here...", min_length=10, max_length=None, required=False))
        self.channel : discord.TextChannel = channel

    async def callback(self, interaction : discord.Interaction):
        rate = self.children[0].value
        details = self.children[1].value
        embed = SuccessEmbed(title="FEEDBACK SENT", description="Thanks for your feedback!")
        await process_feedback(self.channel, rate, details)
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def make_feedback(ctx : commands.Context, channel):
    embed = BotEmbed(title="NEW FEEDBACK", description="Click ✅ to give your feedback!")
    await ctx.send(embed=embed, view=FeedbackView(channel))
async def process_feedback(channel : discord.TextChannel, rate, details):
    embed = FeedbackEmbed()
    embed.add_field(name=f"**Rate :**", value=f"{rate}/5", inline=False)
    if (details):
            embed.add_field(name="**Feedback content :**", value=details, inline=False)
    print(f"  Feedback sent !")
    await channel.send(embed=embed)
