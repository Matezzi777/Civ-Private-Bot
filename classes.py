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

#============================================== MENUS SELECT ================================================
#Menu Select bans pre-draft
class MenuSelectBans1(discord.ui.View):
    options = [
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
        discord.SelectOption(label="Gorgo", value="22", description="Greece", emoji="<:greece_gorgo:1147559840609210418>"),
        discord.SelectOption(label="Hammurabi", value="23", description="Babylon", emoji="<:babylon:1147559837132140734>"),
        discord.SelectOption(label="Harald Hardrada (Konge)", value="24", description="Norway", emoji="<:norway_konge:1147559848255430818>"),
        discord.SelectOption(label="Harald Hardrada (Varangian)", value="25", description="Norway", emoji="<:norway_varangian:1147559850574876742>")
    ]
    @discord.ui.select(placeholder ="Select Color", options=options)
    async def menu_callback(self, select : discord.ui.Select, interaction : discord.Interaction):
        if (select.values[0] == "1"):
            await interaction.response.send_message(content="You choose to ban <:america_abraham:1147559671784280146> **Abraham Lincoln**.")
        elif (select.values[0] == "2"):
            await interaction.response.send_message(content="You choose to ban <:macedon:1147559683876458566> **Alexander**.")
        elif (select.values[0] == "3"):
            await interaction.response.send_message(content="You choose to ban <:nubia:1147559685361246339> **Amanitore**.")
        elif (select.values[0] == "4"):
            await interaction.response.send_message(content="You choose to ban <:gaul:1147559681942892625> **Ambiorix**.")
        elif (select.values[0] == "5"):
            await interaction.response.send_message(content="You choose to ban <:vietnam:1147559688305659924> **Ba Trieu**.")
        elif (select.values[0] == "6"):
            await interaction.response.send_message(content="You choose to ban <:byzantium_bazil:1147559673252290610> **Basil II**.")
        elif (select.values[0] == "7"):
            await interaction.response.send_message(content="You choose to ban <:france_blackqueen:1147559676658057379> **Catherine de Medici (Black Queen)**.")
        elif (select.values[0] == "8"):
            await interaction.response.send_message(content="You choose to ban <:france_magnificent:1147559680315510887> **Catherine de Medici (Magnificent)**.")
        elif (select.values[0] == "9"):
            await interaction.response.send_message(content="You choose to ban <:india_chandragupta:1147559784783040542> **Chandragupta**.")
        elif (select.values[0] == "10"):
            await interaction.response.send_message(content="You choose to ban <:egypt_cleopatra_base:1147559777640128512> **Cleopatra (Egyptian)**.")
        elif (select.values[0] == "11"):
            await interaction.response.send_message(content="You choose to ban <:egypt_cleopatra_ptolemaic:1147559780190261288> **Cleopatra (Ptolemaic)**.")
        elif (select.values[0] == "12"):
            await interaction.response.send_message(content="You choose to ban <:persia_cyrus:1147559790122381312> **Cyrus**.")
        elif (select.values[0] == "13"):
            await interaction.response.send_message(content="You choose to ban <:phenicia:1147559791531671632> **Dido**.")
        elif (select.values[0] == "14"):
            await interaction.response.send_message(content="You choose to ban <:england_eleanor:1147559675278147646> **Eleanor of Aquitaine (England)**.")
        elif (select.values[0] == "15"):
            await interaction.response.send_message(content="You choose to ban <:france_eleanor:1147559678948167700> **Eleanor of Aquitaine (France)**.")
        elif (select.values[0] == "16"):
            await interaction.response.send_message(content="You choose to ban <:england_elizabeth:1147559782094487623> **Elizabeth I**.")
        elif (select.values[0] == "17"):
            await interaction.response.send_message(content="You choose to ban <:germany_barbarossa:1147559839157993483> **Frederick Barbarossa**.")
        elif (select.values[0] == "18"):
            await interaction.response.send_message(content="You choose to ban <:india_gandhi:1147559841745862818> **Gandhi**.")
        elif (select.values[0] == "19"):
            await interaction.response.send_message(content="You choose to ban <:mongolia_genghis:1147559846053433365> **Genghis Khan**.")
        elif (select.values[0] == "20"):
            await interaction.response.send_message(content="You choose to ban <:sumer:1147559854228119624> **Gilgamesh**.")
        elif (select.values[0] == "21"):
            await interaction.response.send_message(content="You choose to ban <:indonesia:1147559786192326796> **Gitarja**.")
        elif (select.values[0] == "22"):
            await interaction.response.send_message(content="You choose to ban <:greece_gorgo:1147559840609210418> **Gorgo**.")
        elif (select.values[0] == "23"):
            await interaction.response.send_message(content="You choose to ban <:babylon:1147559837132140734> **Hammurabi**.")
        elif (select.values[0] == "24"):
            await interaction.response.send_message(content="You choose to ban <:norway_konge:1147559848255430818> **Harald Hardrada (Konge)**.")
        elif (select.values[0] == "25"):
            await interaction.response.send_message(content="You choose to ban <:norway_varangian:1147559850574876742> **Harald Hardrada (Varangian)**.")
        else:
            await interaction.response.send_message(content="Error.")

class MenuSelectBans2(discord.ui.View):
    options = [
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
        discord.SelectOption(label="Mvemba a Nzinga", value="43", description="Kongo", emoji="<:kongo_mvemba:1147559993135075398>"),
        discord.SelectOption(label="Nader Shah", value="44", description="Persia", emoji="<:persia_nader:1147559999015485530>"),
        discord.SelectOption(label="Njinga Mbande", value="45", description="Kongo", emoji="<:kongo_njinga:1147559995622310090>"),
        discord.SelectOption(label="Pachacuti", value="46", description="Inca", emoji="<:pachacutec:1147559997149028352>"),
        discord.SelectOption(label="Pedro II", value="47", description="Brazil", emoji="<:brazil:1147666442427322369>"),
        discord.SelectOption(label="Pericles", value="48", description="Greece", emoji="<:greece_pericles:1147559988940771338>"),
        discord.SelectOption(label="Peter", value="49", description="Russia", emoji="<:russia:1147666452636254329>"),
        discord.SelectOption(label="Philip II", value="50", description="Spain", emoji="<:spain:1147560001020379238>")
    ]
    @discord.ui.select(placeholder ="Select Color", options=options)
    async def menu_callback(self, select : discord.ui.Select, interaction : discord.Interaction):
        if (select.values[0] == "26"):
            await interaction.response.send_message(content="You choose to ban <:japan_hojo:1147559844769976321> **Hojo Tokimune**.")
        elif (select.values[0] == "27"):
            await interaction.response.send_message(content="You choose to ban <:poland:1147559852776886272> **Jadwiga**.")
        elif (select.values[0] == "28"):
            await interaction.response.send_message(content="You choose to ban <:khmer:1147559913657221321> **Jayavarman VII**.")
        elif (select.values[0] == "29"):
            await interaction.response.send_message(content="You choose to ban <:portugal:1147559923543199886> **Joao III**.")
        elif (select.values[0] == "30"):
            await interaction.response.send_message(content="You choose to ban <:australia:1147559905998405682> **John Curtin**.")
        elif (select.values[0] == "31"):
            await interaction.response.send_message(content="You choose to ban <:rome_caesar:1147559926072348703> **Julius Caesar**.")
        elif (select.values[0] == "32"):
            await interaction.response.send_message(content="You choose to ban <:sweden:1147559793708507266> **Kristina**.")
        elif (select.values[0] == "33"):
            await interaction.response.send_message(content="You choose to ban <:china_kubilai:1147559908456284193> **Kubilai Khan (China)**.")
        elif (select.values[0] == "34"):
            await interaction.response.send_message(content="You choose to ban <:mongolia_kubilai:1147559922012270602> **Kubilai Khan (Mongolia)**.")
        elif (select.values[0] == "35"):
            await interaction.response.send_message(content="You choose to ban <:kupe:1147559915456577536> **Kupe**.")
        elif (select.values[0] == "36"):
            await interaction.response.send_message(content="You choose to ban <:mayas:1147559787425435769> **Lady Six Sky**.")
        elif (select.values[0] == "37"):
            await interaction.response.send_message(content="You choose to ban <:mapuche:1147559919562788954> **Lautaro**.")
        elif (select.values[0] == "38"):
            await interaction.response.send_message(content="You choose to ban <:germany_ludwig:1147559910977061015> **Ludwig II**.")
        elif (select.values[0] == "39"):
            await interaction.response.send_message(content="You choose to ban <:mali_mansamoussa:1147559918090600560> **Mansa Musa**.")
        elif (select.values[0] == "40"):
            await interaction.response.send_message(content="You choose to ban <:hungary:1147559991427997826> **Matthias Corvinus**.")
        elif (select.values[0] == "41"):
            await interaction.response.send_message(content="You choose to ban <:ethiopia:1147559987707654265> **Menelik II**.")
        elif (select.values[0] == "42"):
            await interaction.response.send_message(content="You choose to ban <:aztec:1147559983928594578> **Montezuma**.")
        elif (select.values[0] == "43"):
            await interaction.response.send_message(content="You choose to ban <:kongo_mvemba:1147559993135075398> **Mvemba a Nzinga**.")
        elif (select.values[0] == "44"):
            await interaction.response.send_message(content="You choose to ban <:persia_nader:1147559999015485530> **Nader Shah**.")
        elif (select.values[0] == "45"):
            await interaction.response.send_message(content="You choose to ban <:kongo_njinga:1147559995622310090> **Njinga Mbande**.")
        elif (select.values[0] == "46"):
            await interaction.response.send_message(content="You choose to ban <:pachacutec:1147559997149028352> **Pachacuti**.")
        elif (select.values[0] == "47"):
            await interaction.response.send_message(content="You choose to ban <:brazil:1147666442427322369> **Pedro II**.")
        elif (select.values[0] == "48"):
            await interaction.response.send_message(content="You choose to ban <:greece_pericles:1147559988940771338> **Pericles**.")
        elif (select.values[0] == "49"):
            await interaction.response.send_message(content="You choose to ban <:russia:1147666452636254329> **Peter**.")
        elif (select.values[0] == "50"):
            await interaction.response.send_message(content="You choose to ban <:spain:1147560001020379238> **Philip II**.")
        else:
            await interaction.response.send_message(content="Error.")

class MenuSelectBans3(discord.ui.View):
    options = [
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
        discord.SelectOption(label="Tamar", value="64", description="Georgia", emoji="<:georgia:1147666515873775696>"),
        discord.SelectOption(label="Teddy Roosevelt (Bull Moose)", value="65", description="America", emoji="<:america_bullmoose:1147666508613427212>"),
        discord.SelectOption(label="Teddy Roosevelt (Rough Rider)", value="66", description="America", emoji="<:america_roughrider:1147666510890938430>"),
        discord.SelectOption(label="Theodora", value="67", description="Byzantium", emoji="<:byzantium_theodora:1147666512287649802>"),
        discord.SelectOption(label="Tokugawa", value="68", description="Japan", emoji="<:japan_tokugawa:1147666516985253950>"),
        discord.SelectOption(label="Tomyris", value="69", description="Scythia", emoji="<:scythia:1147666576288526408>"),
        discord.SelectOption(label="Trajan", value="70", description="Rome", emoji="<:rome_trajan:1147666574162018334>"),
        discord.SelectOption(label="Victoria (Age of Empire)", value="71", description="England", emoji="<:england_victoria:1147666570458443777>"),
        discord.SelectOption(label="Victoria (Age of Steam)", value="72", description="England", emoji="<:england_ageofsteam:1147666569149808731>"),
        discord.SelectOption(label="Wilfrid Laurier", value="73", description="Canada", emoji="<:canada:1147666565270085673>"),
        discord.SelectOption(label="Wilhelmina", value="74", description="Netherland", emoji="<:netherland:1147666572865966170>"),
        discord.SelectOption(label="Wu Zetian", value="75", description="China", emoji="<:china_wuzetian:1147666567690195125>")
    ]
    @discord.ui.select(placeholder ="Select a leader to ban...", options=options)
    async def menu_callback(self, select : discord.ui.Select, interaction : discord.Interaction):
        if (select.values[0] == "51"):
            await interaction.response.send_message(content="You choose to ban <:cree:1147666447745683467> **Poundmaker**.")
        elif (select.values[0] == "52"):
            await interaction.response.send_message(content="You choose to ban <:china_mandate:1147666444121821304> **Qin (Mandate of Heaven)**.")
        elif (select.values[0] == "53"):
            await interaction.response.send_message(content="You choose to ban <:china_unifier:1147666446508368022> **Qin (Unifier)**.")
        elif (select.values[0] == "54"):
            await interaction.response.send_message(content="You choose to ban <:egypt_ramses:1147666449788325999> **Ramses II**.")
        elif (select.values[0] == "55"):
            await interaction.response.send_message(content="You choose to ban <:scotland:1147666454850834573> **Robert the Bruce**.")
        elif (select.values[0] == "56"):
            await interaction.response.send_message(content="You choose to ban <:arabia_mamelouk:1147666438866350180> **Saladin (Sultan)**.")
        elif (select.values[0] == "57"):
            await interaction.response.send_message(content="You choose to ban <:arabia_vizir:1147666441135468564> **Saladin (Vizier)**.")
        elif (select.values[0] == "58"):
            await interaction.response.send_message(content="You choose to ban <:korea_sejong:1147666451122110505> **Sejong**.")
        elif (select.values[0] == "59"):
            await interaction.response.send_message(content="You choose to ban <:korea_seondeok:1147666519568941168> **Seondeok**.")
        elif (select.values[0] == "60"):
            await interaction.response.send_message(content="You choose to ban <:zulu:1147559794945822730> **Shaka**.")
        elif (select.values[0] == "61"):
            await interaction.response.send_message(content="You choose to ban <:colombia:1147666513453649970> **Simon Bolivar**.")
        elif (select.values[0] == "62"):
            await interaction.response.send_message(content="You choose to ban <:ottoman_magnificent:1147666523759050782> **Suleiman (Kanuni)**.")
        elif (select.values[0] == "63"):
            await interaction.response.send_message(content="You choose to ban <:ottoman_muthesem:1147666525159968918> **Suleiman (Muthesem)**.")
        elif (select.values[0] == "64"):
            await interaction.response.send_message(content="You choose to ban <:georgia:1147666515873775696> **Tamar**.")
        elif (select.values[0] == "65"):
            await interaction.response.send_message(content="You choose to ban <:america_bullmoose:1147666508613427212> **Teddy Roosevelt (Bull Moose)**.")
        elif (select.values[0] == "66"):
            await interaction.response.send_message(content="You choose to ban <:america_roughrider:1147666510890938430> **Teddy Roosevelt (Rough Rider)**.")
        elif (select.values[0] == "67"):
            await interaction.response.send_message(content="You choose to ban <:byzantium_theodora:1147666512287649802> **Theodora**.")
        elif (select.values[0] == "68"):
            await interaction.response.send_message(content="You choose to ban <:japan_tokugawa:1147666516985253950> **Tokugawa**.")
        elif (select.values[0] == "69"):
            await interaction.response.send_message(content="You choose to ban <:scythia:1147666576288526408> **Tomyris**.")
        elif (select.values[0] == "70"):
            await interaction.response.send_message(content="You choose to ban <:rome_trajan:1147666574162018334> **Trajan**.")
        elif (select.values[0] == "71"):
            await interaction.response.send_message(content="You choose to ban <:england_victoria:1147666570458443777> **Victoria (Age of Empire)**.")
        elif (select.values[0] == "72"):
            await interaction.response.send_message(content="You choose to ban <:england_ageofsteam:1147666569149808731> **Victoria (Age of Steam)**.")
        elif (select.values[0] == "73"):
            await interaction.response.send_message(content="You choose to ban <:canada:1147666565270085673> **Wilfrid Laurier**.")
        elif (select.values[0] == "74"):
            await interaction.response.send_message(content="You choose to ban <:netherland:1147666572865966170> **Wilhelmina**.")
        elif (select.values[0] == "75"):
            await interaction.response.send_message(content="You choose to ban <:china_wuzetian:1147666567690195125> **Wu Zetian**.")
        else:
            await interaction.response.send_message(content="Error.")

class MenuSelectBans4(discord.ui.View):
    options = [
        discord.SelectOption(label="Yongle", value="76", description="China", emoji="<:china_yongle:1147559986424205395>"),
        discord.SelectOption(label="Sundiata Keita", value="77", description="Mali", emoji="<:mali_soundiata:1147666521078902817>")
    ]
    @discord.ui.select(placeholder ="Select a leader to ban...", options=options)
    async def menu_callback(self, select : discord.ui.Select, interaction : discord.Interaction):
        if (select.values[0] == "76"):
            await interaction.response.send_message(content="You choose to ban <:china_yongle:1147559986424205395> Yongle.")
        elif (select.values[0] == "77"):
            await interaction.response.send_message(content="You choose to ban <:mali_soundiata:1147666521078902817> Sundiata Keita.")
        else:
            await interaction.response.send_message(content="Error.")

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