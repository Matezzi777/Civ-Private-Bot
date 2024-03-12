#============================================= INITIALISATION ===============================================
#Import des modules
import discord
from discord.ext import commands
from classes import BotEmbed, SuccessEmbed, ErrorEmbed, ValidButton 

#================================================ BOUTONS ===================================================
#Bouton Pangaea 🌋
class Button_pangaea(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🌋 Pangaea",
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
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🌊 Seven Seas",
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
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="⛰️ Highlands",
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
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🌍 Continents",
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
#Bouton Continents and Islands 🏝️
class Button_continents_and_islands(discord.ui.Button):
    def __init__(self, list_users : list, needed_confirm : int) -> None:
        super().__init__(
            label="🏝️ Continents and Islands",
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
                self.label = f"🏝️ Continents and Islands ({self.count})"
                await interaction.response.edit_message(view=self.view)
            else:
                valid_button = ValidButton()
                valid_button.label = "🏝️ Continents and Islands"
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
        self.add_item(Button_pangaea(users, self.needed_confirm))
        self.add_item(Button_seven_seas(users, self.needed_confirm))
        self.add_item(Button_highlands(users, self.needed_confirm))
        self.add_item(Button_continents(users, self.needed_confirm))
        self.add_item(Button_continents_and_islands(users, self.needed_confirm))
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

#=============================================== FONCTIONS ==================================================
#Lance un mapvote
async def make_mapvote(ctx : commands.Context) -> None:
    author = ctx.message.author
    
    #Vérifie que l'utilisateur est bien dans un salon vocal
    if (not author.voice):
        await make_generic_mapvote(ctx)
        return
    else:
        channel = author.voice.channel
        users = channel.members
        nb_users : int = len(users)

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
    #Envoie le message pour le BCY
    await ctx.send("**BCY**", view=BCYView(users))
    #Envoie le message pour l'age du monde
    await ctx.send("**AGE OF THE WORLD**", view=AgeView(users))
    #Envoie le message pour le ridge
    await ctx.send("**RIDGE DEFINITION**", view=RidgeView(users))
    #Envoie le message pour la victoire religieuse
    await ctx.send("**RELIGIOUS VICTORY**", view=ReligionView(users))
    #Envoie le message pour les barbares
    await ctx.send("**BARBARIANS**", view=BarbariansView(users))
#Lance un mapvote générique
async def make_generic_mapvote(ctx : commands.Context) -> None:
    embed = BotEmbed(title="MAPVOTE", description=f"\nReact on the following messages to select the options.")
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
