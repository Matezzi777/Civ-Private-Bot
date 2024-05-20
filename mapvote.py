#============================================= INITIALISATION ===============================================
#Import des modules
import discord
from discord.ext import commands
from discord.ui.item import Item
from classes import BotEmbed, SuccessEmbed, ErrorEmbed, ValidButton 

BBG_STABLE_VERSION : str = "5.8.1"
BBG_BETA_VERSION : str = "BETA"

#================================================ BOUTONS ===================================================
#Bouton Pangaea 🌋
class Button_pangaea(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int, row : int) -> None:
        super().__init__(
            label="🌋 Pangaea",
            style=discord.ButtonStyle.grey,
            row=row
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🌋 Pangaea ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🌋 Pangaea"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Seven Seas 🌊
class Button_seven_seas(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int, row) -> None:
        super().__init__(
            label="🌊 Seven Seas",
            style=discord.ButtonStyle.grey,
            row=row
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🌊 Seven Seas ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🌊 Seven Seas"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Highlands ⛰️
class Button_highlands(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int, row : int) -> None:
        super().__init__(
            label="⛰️ Highlands",
            style=discord.ButtonStyle.grey,
            row=row
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"⛰️ Highlands ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "⛰️ Highlands"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Continents 🌍
class Button_continents(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int, row : int) -> None:
        super().__init__(
            label="🌍 Continents",
            style=discord.ButtonStyle.grey,
            row=row
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🌍 Continents ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🌍 Continents"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton TSL 🗺️
class Button_tsl(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int, row : int) -> None:
        super().__init__(
            label="🗺️ True Start Locations",
            style=discord.ButtonStyle.grey,
            row=row
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🗺️ True Start Locations ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🗺️ True Start Locations"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Lakes ⛵
class Button_lakes(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int, row : int) -> None:
        super().__init__(
            label="⛵ Lakes",
            style=discord.ButtonStyle.grey,
            row=row
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"⛵ Lakes ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "⛵ Lakes"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Continents & Islands 🏝️
class Button_continents_and_islands(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int, row : int) -> None:
        super().__init__(
            label="🏝️ Continents & Islands",
            style=discord.ButtonStyle.grey,
            row=row
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🏝️ Continents & Islands ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🏝️ Continents & Islands"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Rich Highlands 🌄
class Button_rich_highlands(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int, row : int) -> None:
        super().__init__(
            label="🌄 Rich Highlands",
            style=discord.ButtonStyle.grey,
            row=row
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🌄 Rich Highlands ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🌄 Rich Highlands"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Snowflake ❄️
class Button_snowflake(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int, row : int) -> None:
        super().__init__(
            label="❄️ Snowflake",
            style=discord.ButtonStyle.grey,
            row=row
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"❄️ Snowflake ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "❄️ Snowflake"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Inland Sea 🧜‍♀️
class Button_inland_sea(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int, row : int) -> None:
        super().__init__(
            label="🧜‍♀️ Inland Sea",
            style=discord.ButtonStyle.grey,
            row=row
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🧜‍♀️ Inland Sea ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🧜‍♀️ Inland Sea"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)



#Bouton ON ✅
class Button_on(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="✅ ON",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"✅ ON ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "✅ ON"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton OFF ❌
class Button_off(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="❌ OFF",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"❌ OFF ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "❌ OFF"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Cap Only ⭐
class Button_cap_only(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="⭐ Cap Only",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"⭐ Cap Only ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "⭐ Cap Only"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton All cities 🏙️
class Button_all_cities(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🏙️ All Cities",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🏙️ All Cities ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🏙️ All Cities"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton New 🏔️
class Button_new(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🏔️ New",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🏔️ New ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🏔️ New"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Standard (Age)🗻
class Button_standard_age(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🗻 Standard",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🗻 Standard ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🗻 Standard"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Standard (Ridge) 🔴
class Button_standard_ridge(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🔴 Standard",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🔴 Standard ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🔴 Standard"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Old 🌄
class Button_old(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🌄 Old",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🌄 Old ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🌄 Old"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Classic 🔺
class Button_classic(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🔺 Classic",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🔺 Classic ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🔺 Classic"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Standard (Barbarians) ⚔️
class Button_standard_barbs(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="⚔️ Standard",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"⚔️ Standard ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "⚔️ Standard"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Civilized 👔
class Button_civilized(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="👔 Civilized",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"👔 Civilized ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "👔 Civilized"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)

#Bouton BBG 
class Button_BBG(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label=f"💪 {BBG_STABLE_VERSION}",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"💪 {BBG_STABLE_VERSION} ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = f"💪 {BBG_STABLE_VERSION}"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton BBG Beta
class Button_BBGBeta(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label=f"🔎 {BBG_BETA_VERSION}",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🔎 {BBG_BETA_VERSION} ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = f"🔎 {BBG_BETA_VERSION}"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)

#Bouton BBG 
class Button_FFA(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label=f"🙍‍♂️ FFA",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🙍‍♂️ FFA ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = f"🙍‍♂️ FFA"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton BBG Beta
class Button_Teamer(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label=f"👪 Teamer",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"👪 Teamer ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = f"👪 Teamer"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)

#Bouton Large Opening 🐴
class Button_Ridge_Large(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🐴 Large Opening",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🐴 Large Opening ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🐴 Large Opening"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Bouton Impenetrable 🏰
class Button_Ridge_Impenetrable(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🏰 Impenetrable",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🏰 Impenetrable ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🏰 Impenetrable"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)

#Button Casual Timer 🦥
class Button_Casu_Timer(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🦥 Casual",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🦥 Casual ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🦥 Casual"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Button Classic Timer ⏲
class Button_Classic_Timer(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="⏲ Classic",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"⏲ Classic ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "⏲ Classic"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Button Competitive Timer ⚡
class Button_Competitive_Timer(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="⚡ Competitive",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"⚡ Competitive ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "⚡ Competitive"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)

#Button Scarse 🏜️
class Button_Sparse(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🏜️ Sparse",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🏜️ Sparse ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🏜️ Sparse"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Button Standard Density ☀️
class Button_Standard_Density(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="☀️ Standard",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"☀️ Standard ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "☀️ Standard"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Button Abundant Density 🌞
class Button_Abundant(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🌞 Abundant",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🌞 Abundant ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🌞 Abundant"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Button Epic Density 🌈
class Button_Epic(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🌈 Epic",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"🌈 Epic ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🌈 Epic"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)
#Button Spawn Guaranteed Density ⚔
class Button_Spawn_Garanteed(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="⚔ Spawn Guaranteed",
            style=discord.ButtonStyle.grey
        )
        self.list_users : list = list_users
        self.needed_confirm : int = needed_confirm
        self.count = 0
        self.users_who_clicked : list = []

    async def callback(self, interaction : discord.Interaction) -> None:
        user = interaction.user
        if (user in self.list_users):
            if (not user in self.users_who_clicked):
                self.count = self.count + 1
                self.users_who_clicked.append(user)
            else:
                self.count = self.count - 1
                self.users_who_clicked.remove(user)
            if (self.count < self.needed_confirm):
                self.label = f"⚔ Spawn Guaranteed ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "⚔ Spawn Guaranteed"
                valid_view = discord.ui.View()
                valid_view.add_item(valid_button)
                await interaction.response.edit_message(view=valid_view)
        else:
            embed = ErrorEmbed(description="You tried to vote for a mapvote, but you are not in this game.\nIf you want to join the game, hop in the Voice Channel and ask for a new mapvote.")
            await user.send(embed=embed)
            await interaction.response.edit_message(view=self.view)

#================================================= VIEWS ====================================================
#View DRAFT
class DraftView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_on(users, self.needed_confirm))
        self.add_item(Button_off(users, self.needed_confirm))

#View MAP
class MapView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_pangaea(users, self.needed_confirm, row=0))
        self.add_item(Button_seven_seas(users, self.needed_confirm, row=0))
        self.add_item(Button_highlands(users, self.needed_confirm, row=0))
        self.add_item(Button_continents(users, self.needed_confirm, row=0))
        self.add_item(Button_tsl(users, self.needed_confirm, row=0))
        self.add_item(Button_lakes(users, self.needed_confirm, row=1))
        self.add_item(Button_rich_highlands(users, self.needed_confirm, row=1))
        self.add_item(Button_continents_and_islands(users, self.needed_confirm, row=1))
        self.add_item(Button_inland_sea(users, self.needed_confirm, row=1))
        self.add_item(Button_snowflake(users, self.needed_confirm, row=1))
#View BCY
class BCYView(discord.ui.View):
   def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_cap_only(users, self.needed_confirm))
        self.add_item(Button_all_cities(users, self.needed_confirm))
        self.add_item(Button_off(users, self.needed_confirm))
#View Age
class AgeView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_new(users, self.needed_confirm))
        self.add_item(Button_standard_age(users, self.needed_confirm))
        self.add_item(Button_old(users, self.needed_confirm))
#View Ridge
class RidgeView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_standard_ridge(users, self.needed_confirm))
        self.add_item(Button_classic(users, self.needed_confirm))
        self.add_item(Button_Ridge_Large(users, self.needed_confirm))
        self.add_item(Button_Ridge_Impenetrable(users, self.needed_confirm))
#View Religion
class ReligionView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_on(users, self.needed_confirm))
        self.add_item(Button_off(users, self.needed_confirm))
#View Barbares
class BarbariansView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_standard_barbs(users, self.needed_confirm))
        self.add_item(Button_civilized(users, self.needed_confirm))
        self.add_item(Button_off(users, self.needed_confirm))
#View Version BBG
class VersionView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_BBG(users, self.needed_confirm))
        self.add_item(Button_BBGBeta(users, self.needed_confirm))
#View Format
class FormatView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_FFA(users, self.needed_confirm))
        self.add_item(Button_Teamer(users, self.needed_confirm))
#View Forest Balancing
class ForestBalancingView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_on(users, self.needed_confirm))
        self.add_item(Button_off(users, self.needed_confirm))
#View Timer
class TimerView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_Casu_Timer(users, self.needed_confirm))
        self.add_item(Button_Classic_Timer(users, self.needed_confirm))
        self.add_item(Button_Competitive_Timer(users, self.needed_confirm))

#View Density
class DensityView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_Sparse(users, self.needed_confirm))
        self.add_item(Button_Standard_Density(users, self.needed_confirm))
        self.add_item(Button_Abundant(users, self.needed_confirm))

#View StratDensity
class StratDensityView(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(timeout=None)
        self.nb_users : int = len(users)
        self.needed_confirm : int = (self.nb_users // 2) + 1
        self.add_item(Button_Standard_Density(users, self.needed_confirm))
        self.add_item(Button_Abundant(users, self.needed_confirm))
        self.add_item(Button_Epic(users, self.needed_confirm))
        self.add_item(Button_Spawn_Garanteed(users, self.needed_confirm))


#=============================================== FONCTIONS ==================================================
#Lance un mapvote
async def make_mapvote(ctx : commands.Context, voice_channel : discord.VoiceChannel) -> None:
    author = ctx.message.author
    
    #Vérifie que l'utilisateur est bien dans un salon vocal
    if (not author.voice):
        embed = BotEmbed(title=f"🎤 JOIN A VOICE CHANNEL 🎤", description=f"Please, join a voice channel with the other players to use this command.")
        return await ctx.send(embed=embed)
    else:
        channel = author.voice.channel
        users = channel.members
        nb_users : int = len(users)
        for user in users:
            await user.move_to(voice_channel)

    #Mentionne tous les membres du salon vocal
    message = ""
    i : int = 0
    while (i < nb_users):
        message = message + f"{users[i].mention} "
        i = i + 1
    message = f"Let's vote !\n\n*{nb_users}* players in the game :\n" + message
    await ctx.send(message)

    #Envoie le message pour la version
    await ctx.send("**BBG VERSION**", view=VersionView(users))
    #Envoie le message du fortmay (FFA / Teamer)
    await ctx.send("**FORMAT**", view=FormatView(users))
    #Envoie le message pour les drafts
    await ctx.send("**DRAFT**", view=DraftView(users))
    #Envoie le message pour le BCY
    await ctx.send("**BCY**", view=BCYView(users))
    #Envoie le message pour la map
    await ctx.send("**MAP**", view=MapView(users))
    #Envoie le message pour le Forest Balancing
    await ctx.send("**FOREST BALANCING**", view=ForestBalancingView(users))
    #Envoie le message pour l'age du monde
    await ctx.send("**AGE OF THE WORLD**", view=AgeView(users))
    #Envoie le message pour le ridge
    await ctx.send("**RIDGE DEFINITION**", view=RidgeView(users))
    #Envoie le message pour la victoire religieuse
    await ctx.send("**RELIGIOUS VICTORY**", view=ReligionView(users))
    #Envoie le message pour les barbares
    await ctx.send("**BARBARIANS**", view=BarbariansView(users))
#Lance un mapvote plus long
async def make_longer_mapvote(ctx : commands.Context, voice_channel : discord.VoiceChannel) -> None:
    author = ctx.message.author
    
    #Vérifie que l'utilisateur est bien dans un salon vocal
    if (not author.voice):
        embed = BotEmbed(title=f"🎤 JOIN A VOICE CHANNEL 🎤", description=f"Please, join a voice channel with the other players to use this command.")
        return await ctx.send(embed=embed)
    else:
        channel = author.voice.channel
        users = channel.members
        nb_users : int = len(users)
        for user in users:
            await user.move_to(voice_channel)

    #Mentionne tous les membres du salon vocal
    message = ""
    i : int = 0
    while (i < nb_users):
        message = message + f"{users[i].mention} "
        i = i + 1
    message = f"Let's vote !\n\n*{nb_users}* players in the game :\n" + message
    await ctx.send(message)

    #Envoie le message pour la version
    await ctx.send("**BBG VERSION**", view=VersionView(users))
    #Envoie le message du fortmay (FFA / Teamer)
    await ctx.send("**FORMAT**", view=FormatView(users))
    #Envoie le message pour les drafts
    await ctx.send("**DRAFT**", view=DraftView(users))
    #Envoie le message pour le BCY
    await ctx.send("**BCY**", view=BCYView(users))
    #Envoie le message pour le timer
    await ctx.send("**TIMER**", view=TimerView(users))
    #Envoie le message pour la map
    await ctx.send("**MAP**", view=MapView(users))
    #Envoie le message pour les ressources stratégiques
    await ctx.send("**STRATEGIC RESOURCES DENSITY**", view=StratDensityView(users))
    #Envoie le message pour les ressources
    await ctx.send("**RESOURCES DENSITY**", view=DensityView(users))
    #Envoie le message pour la densité des merveilles naturelles
    await ctx.send("**WONDERS DENSITY**", view=DensityView(users))
    #Envoie le message pour le Forest Balancing
    await ctx.send("**FOREST BALANCING**", view=ForestBalancingView(users))
    #Envoie le message pour l'age du monde
    await ctx.send("**AGE OF THE WORLD**", view=AgeView(users))
    #Envoie le message pour le ridge
    await ctx.send("**RIDGE DEFINITION**", view=RidgeView(users))
    #Envoie le message pour la victoire religieuse
    await ctx.send("**RELIGIOUS VICTORY**", view=ReligionView(users))
    #Envoie le message pour les barbares
    await ctx.send("**BARBARIANS**", view=BarbariansView(users))
#Lance un mapvote plus court
async def make_shorter_mapvote(ctx : commands.Context, voice_channel : discord.VoiceChannel) -> None:
    author = ctx.message.author
    
    #Vérifie que l'utilisateur est bien dans un salon vocal
    if (not author.voice):
        embed = BotEmbed(title=f"🎤 JOIN A VOICE CHANNEL 🎤", description=f"Please, join a voice channel with the other players to use this command.")
        return await ctx.send(embed=embed)
    else:
        channel = author.voice.channel
        users = channel.members
        nb_users : int = len(users)
        for user in users:
            await user.move_to(voice_channel)

    #Mentionne tous les membres du salon vocal
    message = ""
    i : int = 0
    while (i < nb_users):
        message = message + f"{users[i].mention} "
        i = i + 1
    message = f"Let's vote !\n\n*{nb_users}* players in the game :\n" + message
    await ctx.send(message)
    
    #Envoie le message pour les drafts
    await ctx.send("**DRAFT**", view=DraftView(users))
    #Envoie le message pour la map
    await ctx.send("**MAP**", view=MapView(users))
    #Envoie le message pour la victoire religieuse
    await ctx.send("**RELIGIOUS VICTORY**", view=ReligionView(users))
    #Envoie le message pour les barbares
    await ctx.send("**BARBARIANS**", view=BarbariansView(users))