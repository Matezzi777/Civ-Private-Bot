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

class BansEmbed(discord.Embed):
    def __init__(self, users : list[discord.User], waiting_for : list[discord.User]) -> None:
        super().__init__(
            colour=discord.Colour.purple(),
            color=discord.Colour.red(),
            title="SELECT BANS",
            type='rich',
            url=None,
            description="Let's vote for bans !",
            timestamp=None
        )
        self.nb_users = len(users)
        self.needed_votes = (self.nb_users//2) + 1
        self.str_mentions = ""
        self.str_waiting_for_mentions = ""
        i : int = 0
        while (i < self.nb_users):
            self.str_mentions = self.str_mentions + f"{users[i].mention} "
            i = i + 1
        i = 0
        while (i < len(waiting_for)):
            self.str_waiting_for_mentions = self.str_waiting_for_mentions + f"{waiting_for[i].mention} "
            i = i + 1
        self.add_field(name="**🎮Players in the game🎮**", value=self.str_mentions)
        self.add_field(name="**❔How to ban civs❔**", value="1. Select the leaders you want to propose to ban.\n2. Confirm your choice.", inline=False)
        self.add_field(name="**⏲Waiting for...**", value=self.str_waiting_for_mentions)
        

#================================================== BANS ====================================================
#View Select Bans
class Bans(discord.ui.View):
    def __init__(self, users) -> None:
        super().__init__(
            timeout=600
        )
        self.users = users
        self.nb_users : int = len(users)
        self.waiting_for : list[discord.User] = users
        self.users_who_already_confirmed : list[discord.User] = []
        self.selected_bans : list = []
        self.add_item(SelectBans(1))
        self.add_item(SelectBans(2))
        self.add_item(SelectBans(3))
        self.add_item(SelectBans(4))
        self.add_item(ConfirmBansButton())
        self.add_item(NoBansButton())

#SelectMenu Bans
class SelectBans(discord.ui.Select):
    def __init__(self, page : int) -> None:
        super().__init__(
            min_values=0,
            max_values=5
        )
        self.page = page
        self.users_who_already_selected : list[discord.User] = []
        #Sélectionne la page à afficher
        if (page == 1):
            self.placeholder="A - G"
            self.options = [
                discord.SelectOption(label="Abraham Lincoln", value="1", description="America", emoji="<:america_abraham:1147559671784280146>"),
                discord.SelectOption(label="Alexander", value="2", description="Macedon", emoji="<:macedon:1147559683876458566>"),
                discord.SelectOption(label="Amanitore", value="3", description="Nubia", emoji="<:nubia:1147559685361246339>"),
                discord.SelectOption(label="Ambiorix", value="4", description="Gaul", emoji="<:gaul:1147559681942892625>"),
                discord.SelectOption(label="Ba Trieu", value="5", description="Vietnam", emoji="<:vietnam:1147559688305659924>"),
                discord.SelectOption(label="Basil II", value="6", description="Byzantium", emoji="<:byzantium_bazil:1147559673252290610>"),
                discord.SelectOption(label="Catherine de Medici (Black Queen)", value="7", description="France", emoji="<:france_blackqueen:1147559676658057379>"),
                discord.SelectOption(label="Catherine de Medici (Magnificence)", value="8", description="France", emoji="<:france_magnificent:1147559680315510887>"),
                discord.SelectOption(label="Chandragupta", value="9", description="India", emoji="<:india_chandragupta:1147559784783040542>"),
                discord.SelectOption(label="Cleopatra (Egyptian)", value="10", description="Egypt", emoji="<:egypt_cleopatra_base:1147559777640128512>"),
                discord.SelectOption(label="Cleopatra (Ptolemaic)", value="11", description="Egypt", emoji="<:egypt_cleopatra_ptolemaic:1147559780190261288>"),
                discord.SelectOption(label="Cyrus", value="12", description="Persia", emoji="<:persia_cyrus:1147559790122381312>"),
                discord.SelectOption(label="Dido", value="13", description="Phoenicia", emoji="<:phenicia:1147559791531671632>"),
                discord.SelectOption(label="Eleanor of Aquitaine", value="14", description="England", emoji="<:england_eleanor:1147559675278147646>"),
                discord.SelectOption(label="Eleanor of Aquitaine", value="15", description="France", emoji="<:france_eleanor:1147559678948167700>"),
                discord.SelectOption(label="Elizabeth I", value="16", description="England", emoji="<:england_elizabeth:1147559782094487623>"),
                discord.SelectOption(label="Frederick Barbarossa", value="17", description="Germany", emoji="<:germany_barbarossa:1147559839157993483>"),
                discord.SelectOption(label="Gandhi", value="18", description="India", emoji="<:india_gandhi:1147559841745862818>"),
                discord.SelectOption(label="Genghis Khan", value="19", description="Mongolia", emoji="<:mongolia_genghis:1147559846053433365>"),
                discord.SelectOption(label="Gilgamesh", value="20", description="Sumeria", emoji="<:sumer:1147559854228119624>"),
                discord.SelectOption(label="Gitarja", value="21", description="Indonesia", emoji="<:indonesia:1147559786192326796>"),
                discord.SelectOption(label="Gorgo", value="22", description="Greece", emoji="<:greece_gorgo:1147559840609210418>")
            ]
        elif (page == 2):
            self.placeholder="H - M"
            self.options = [
                discord.SelectOption(label="Hammurabi", value="23", description="Babylon", emoji="<:babylon:1147559837132140734>"),
                discord.SelectOption(label="Harald Hardrada (Konge)", value="24", description="Norway", emoji="<:norway_konge:1147559848255430818>"),
                discord.SelectOption(label="Harald Hardrada (Varangian)", value="25", description="Norway", emoji="<:norway_varangian:1147559850574876742>"),
                discord.SelectOption(label="Hojo Tokimune", value="26", description="Japan", emoji="<:japan_hojo:1147559844769976321>"),
                discord.SelectOption(label="Jadwiga", value="27", description="Poland", emoji="<:poland:1147559852776886272>"),
                discord.SelectOption(label="Jayavarman VII", value="28", description="Khmer", emoji="<:khmer:1147559913657221321>"),
                discord.SelectOption(label="Joao III", value="29", description="Portugal", emoji="<:portugal:1147559923543199886>"),
                discord.SelectOption(label="John Curtin", value="30", description="Australia", emoji="<:australia:1147559905998405682>"),
                discord.SelectOption(label="Julius Caesar", value="31", description="Rome", emoji="<:rome_caesar:1147559926072348703>"),
                discord.SelectOption(label="Kristina", value="32", description="Sweden", emoji="<:sweden:1147559793708507266>"),
                discord.SelectOption(label="Kubilai Khan", value="33", description="China", emoji="<:china_kubilai:1147559908456284193>"),
                discord.SelectOption(label="Kubilai Khan", value="34", description="Mongolia", emoji="<:mongolia_kubilai:1147559922012270602>"),
                discord.SelectOption(label="Kupe", value="35", description="Maori", emoji="<:kupe:1147559915456577536>"),
                discord.SelectOption(label="Lady Six Sky", value="36", description="Maya", emoji="<:mayas:1147559787425435769>"),
                discord.SelectOption(label="Lautaro", value="37", description="Mapuche", emoji="<:mapuche:1147559919562788954>"),
                discord.SelectOption(label="Ludwig II", value="38", description="Germany", emoji="<:germany_ludwig:1147559910977061015>"),
                discord.SelectOption(label="Mansa Musa", value="39", description="Mali", emoji="<:mali_mansamoussa:1147559918090600560>"),
                discord.SelectOption(label="Matthias Corvinus", value="40", description="Hungary", emoji="<:hungary:1147559991427997826>"),
                discord.SelectOption(label="Menelik II", value="41", description="Ethiopia", emoji="<:ethiopia:1147559987707654265>"),
                discord.SelectOption(label="Montezuma", value="42", description="Aztec", emoji="<:aztec:1147559983928594578>"),
                discord.SelectOption(label="Mvemba a Nzinga", value="43", description="Kongo", emoji="<:kongo_mvemba:1147559993135075398>")
            ]
        elif (page == 3):
            self.placeholder="N - S"
            self.options = [
                discord.SelectOption(label="Nader Shah", value="44", description="Persia", emoji="<:persia_nader:1147559999015485530>"),
                discord.SelectOption(label="Njinga Mbande", value="45", description="Kongo", emoji="<:kongo_njinga:1147559995622310090>"),
                discord.SelectOption(label="Pachacuti", value="46", description="Inca", emoji="<:pachacutec:1147559997149028352>"),
                discord.SelectOption(label="Pedro II", value="47", description="Brazil", emoji="<:brazil:1147666442427322369>"),
                discord.SelectOption(label="Pericles", value="48", description="Greece", emoji="<:greece_pericles:1147559988940771338>"),
                discord.SelectOption(label="Peter", value="49", description="Russia", emoji="<:russia:1147666452636254329>"),
                discord.SelectOption(label="Philip II", value="50", description="Spain", emoji="<:spain:1147560001020379238>"),
                discord.SelectOption(label="Poundmaker", value="51", description="Cree", emoji="<:cree:1147666447745683467>"),
                discord.SelectOption(label="Qin (Mandate of Heaven)", value="52", description="China", emoji="<:china_mandate:1147666444121821304>"),
                discord.SelectOption(label="Qin (Unifier)", value="53", description="China", emoji="<:china_unifier:1147666446508368022>"),
                discord.SelectOption(label="Ramses II", value="54", description="Egypt", emoji="<:egypt_ramses:1147666449788325999>"),
                discord.SelectOption(label="Robert the Bruce", value="55", description="Scotland", emoji="<:scotland:1147666454850834573>"),
                discord.SelectOption(label="Saladin (Sultan)", value="56", description="Arabia", emoji="<:arabia_mamelouk:1147666438866350180>"),
                discord.SelectOption(label="Saladin (Vizier)", value="57", description="Arabia", emoji="<:arabia_vizir:1147666441135468564>"),
                discord.SelectOption(label="Sejong", value="58", description="Korea", emoji="<:korea_sejong:1147666451122110505>"),
                discord.SelectOption(label="Seondeok", value="59", description="Korea", emoji="<:korea_seondeok:1147666519568941168>"),
                discord.SelectOption(label="Shaka", value="60", description="Zulu", emoji="<:zulu:1147559794945822730>"),
                discord.SelectOption(label="Simon Bolivar", value="61", description="Gran Colombia", emoji="<:colombia:1147666513453649970>"),
                discord.SelectOption(label="Suleiman (Kanuni)", value="62", description="Ottoman", emoji="<:ottoman_magnificent:1147666523759050782>"),
                discord.SelectOption(label="Suleiman (Muhtesem)", value="63", description="Ottoman", emoji="<:ottoman_muthesem:1147666525159968918>"),
                discord.SelectOption(label="Sundiata Keita", value="64", description="Mali", emoji="<:mali_soundiata:1147666521078902817>")
            ]
        elif (page == 4):
            self.placeholder="T - Z"
            self.options = [
                discord.SelectOption(label="Tamar", value="65", description="Georgia", emoji="<:georgia:1147666515873775696>"),
                discord.SelectOption(label="Teddy Roosevelt (Bull Moose)", value="66", description="America", emoji="<:america_bullmoose:1147666508613427212>"),
                discord.SelectOption(label="Teddy Roosevelt (Rough Rider)", value="67", description="America", emoji="<:america_roughrider:1147666510890938430>"),
                discord.SelectOption(label="Theodora", value="68", description="Byzantium", emoji="<:byzantium_theodora:1147666512287649802>"),
                discord.SelectOption(label="Tokugawa", value="69", description="Japan", emoji="<:japan_tokugawa:1147666516985253950>"),
                discord.SelectOption(label="Tomyris", value="70", description="Scythia", emoji="<:scythia:1147666576288526408>"),
                discord.SelectOption(label="Trajan", value="71", description="Rome", emoji="<:rome_trajan:1147666574162018334>"),
                discord.SelectOption(label="Victoria (Age of Empire)", value="72", description="England", emoji="<:england_victoria:1147666570458443777>"),
                discord.SelectOption(label="Victoria (Age of Steam)", value="73", description="England", emoji="<:england_ageofsteam:1147666569149808731>"),
                discord.SelectOption(label="Wilfrid Laurier", value="74", description="Canada", emoji="<:canada:1147666565270085673>"),
                discord.SelectOption(label="Wilhelmina", value="75", description="Netherland", emoji="<:netherland:1147666572865966170>"),
                discord.SelectOption(label="Wu Zetian", value="76", description="China", emoji="<:china_wuzetian:1147666567690195125>"),
                discord.SelectOption(label="Yongle", value="77", description="China", emoji="<:china_yongle:1147559986424205395>")
            ]
        else:
            print("    Error Select Page Invalid (must be between 1 and 4).")
    
    async def callback(self, interaction : discord.Interaction):
        user = interaction.user
        if (not user in self.view.users):
            embed = ErrorEmbed(title="YOUR ARE NOT IN THIS GAME", description="You tried to choose leaders to ban for a game which does not concern you.")
            await interaction.response.edit_message(view=self.view)
            await interaction.followup.send(embed=embed, ephemeral=True)
            print(f"    @{user.name} tried to choose leaders to ban for a game which does not concern them.")
            return
        elif (user in self.view.users_who_already_confirmed):
            embed = ErrorEmbed(title="PROPOSITION ALREADY SENT", description="Your already sent a proposition !\nPlease, wait for the other players to finish their choices.")
            await interaction.response.edit_message(view=self.view)
            await interaction.followup.send(embed=embed, ephemeral=True)
            print(f"    @{user.name} tried to select new leaders but has already validated")
            return
        elif (user in self.users_who_already_selected):
            embed = ErrorEmbed(title="ALREADY PICKED IN THIS LIST", description=f"You already picked in the [{self.placeholder}] list.")
            await interaction.response.edit_message(view=self.view)
            await user.send(embed=embed)
            return
        else:
            print(f"    @{user.name} added leaders to his selection")
            return_message : str = ""
            i : int = 0
            while (i < len(self.values)):
                return_message = return_message + f"{self.values[i]}, "
                if (not self.values[i] in self.view.selected_bans):
                    self.view.selected_bans.append(self.values[i])
                    print(f"        {self.values[i]} added")
                else:
                    print(f"        {self.values[i]} already in the list.")
                i = i + 1
            self.users_who_already_selected.append(user)
            return_message = return_message[:-2] + " added to your selection."
            embed=BansEmbed(self.view.users, self.view.waiting_for)
            await interaction.response.edit_message(view=self.view)
            embed=SuccessEmbed(description=return_message)
            await user.send(embed=embed)
            return

#Bouton de validation des Bans
class ConfirmBansButton(discord.ui.Button):
    def __init__(self) -> None:
        super().__init__(
            label="✅ Send your proposition",
            style=discord.ButtonStyle.green
        )
        self.count = 0

    async def callback(self, interaction : discord.Interaction):
        user = interaction.user
        if (not user in self.view.users):
            embed = ErrorEmbed(title="YOUR ARE NOT IN THIS GAME", description="You tried to send a ban proposition for a game which does not concern you.")
            await interaction.response.edit_message(view=self.view)
            await interaction.followup.send(embed=embed, ephemeral=True)
            print(f"    @{user.name} tried to send a proposition for a game which does not concern them.")
            return
        elif (not user in self.view.users_who_already_confirmed):
            print(f"    @{interaction.user.name} sent his proposition")
            self.view.waiting_for.remove(user)
            self.view.users_who_already_confirmed.append(user)
            self.count = self.count + 1

            bans_embed = BansEmbed(self.view.users ,self.view.waiting_for)
            success_embed = SuccessEmbed(title="PROPOSITION SENT", description="Proposition confirmed !\nPlease, wait for the other players to finish their choices.")

            if (self.count == self.view.nb_users):
                self.view.clear_items()
                valid_button = ValidButton()
                valid_button.label="✅ Confirmed"
                self.view.add_item(valid_button)
                print("    All players sent their choices")
                await interaction.response.edit_message(embed=bans_embed, view=self.view)
                await interaction.followup.send(content="LET'S VOTE !")
                return
            else:
                await interaction.response.edit_message(embed=bans_embed, view=self.view)
                await interaction.followup.send(embed=success_embed, ephemeral=True)
                return

        else:
            embed = ErrorEmbed(title="PROPOSITION ALREADY SENT", description="Your already sent a proposition !\nPlease, wait for the other players to finish their choices.")
            await interaction.response.edit_message(view=self.view)
            await interaction.send(embed=embed, ephemeral=True)
            print(f"    @{user.name} already validated")
            return

class NoBansButton(discord.ui.Button):
    def __init__(self) -> None:
        super().__init__(
            label="❌ No bans",
            style=discord.ButtonStyle.red
        )
    
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        if (not user in self.view.users):
            embed = ErrorEmbed(title="YOUR ARE NOT IN THIS GAME", description="You tried to send a ban proposition for a game which does not concern you.")
            await interaction.response.edit_message(view=self.view)
            await interaction.followup.send(embed=embed, ephemeral=True)
            print(f"    @{user.name} tried to send a proposition for a game which does not concern them.")
            return
        elif (not user in self.view.waiting_users):
            embed = SuccessEmbed(title="PROPOSITION SENT", description="You choose to not ban leaders.\nPlease, wait for the other players to finish their choices.")
            await interaction.response.edit_message(view=self.view)
            self.view.waiting_users.append(user)
            await interaction.followup.send(embed=embed, ephemeral=True)
            print(f"    @{interaction.user.name} sent his proposition (No Bans)")
            return
        else:
            embed = ErrorEmbed(title="PROPOSITION ALREADY SENT", description="Your already sent a proposition !\nPlease, wait for the other players to finish their choices.")
            await interaction.response.edit_message(view=self.view)
            await interaction.followup.send(embed=embed, ephemeral=True)
            print(f"    @{user.name} already validated")
            return

#================================================ BUTTONS ===================================================
#Bouton choix validé générique
class ValidButton(discord.ui.Button):
    def __init__(self) -> None:
        super().__init__(
            label=" - ",
            style=discord.ButtonStyle.green
        )
    
    async def callback(self, interaction : discord.Interaction):
        await interaction.response.edit_message(view=self.view)
