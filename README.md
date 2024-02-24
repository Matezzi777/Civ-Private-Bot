# Getting Started :
1. Create a database named *db.sqlite* at the root of the project.
2. Create a table named *Anniversaires* containing the following columns (User_ID : integer, Date : integer) in *db.sqlite*
3. Create a table named *Ranked* containing the following columns (User_ID : text, Elo : integer, Wins : integer, Top1 : integer, Lost : integer, Date : datetime) in *db.sqlite*
4. Rock n'Roll !

## BOT INFORMATIONS :
- Bot Name : Civ Private Bot
- Bot Prefix : $
- Bot Intents : Admin (all)
- Bot Description : "Civ Private Bot v2.0.0"

## COMMANDS SUMMARY (CivPrivateBot.py) :
* **Informations**
  - $hello : send a little hello message in the current channel (more like an Easter Egg).
  - $serverinfo : send some informations about the server in the current channel.
  - $clear (x : int) : delete the last x messages of the current channel.
  - $datenow : send the date in the current channel.
* **Drafts & mapvote**
  - $draft (x : int) : draw x civs to all the players in the same voice chat than the caller of the command and send the result in the current channel.
  - $blind_draft (x : int) : draw x civs to all the players in the same voice chat than the caller of the command and send the result in private message to each one.
  - $generic_draft (x : int, y : int) : draw x civ to y players and send the result in the current channel.
  - $mapvote : start a mapvote in the current channel (Voice Channel recommended).
  - $generic_mapvote : start a generic mapvote in the current channel.
* **Birthdays**
  - $set_birthday (date : str) : set the birthday of the caller of the function to the indicated date (use DDMM format (ex: 13th of March -> 1303)).
  - $rm_birthday : delete the birthday of the caller of the function from the database.
  - $birthdays : displays the birthdays from the database in the current channel.
* **Ranked**
  - $report (users : list) : report the result of a ranked game (mention the player in the same order than the scoreboard at the end of the game (winner first anyway)).
  - $stats : display the stats of the caller of the function in the current channel.
  - $leaderboard : update the leaderboard in the leaderboard channel.
  - $setup_leaderboard : create the leaderboard in the indicated channel (in order to update later).

## FUNCTIONS SUMMARY :
* **birthdays.py**
  - add_birthday(user, date)
  - rem_birthday(user)
  - display_birthdays
  - display_date
  - change_birthday(user, date)
  - get_birthday(user)
  - parse_date(date)
  - check_birthday(user)
* **drafts.py**
  - make_draft(nb_civs)
  - make_blind_draft(nb_civs)
  - make_generic_draft(nb_players, nb_civs)
  - create_draft(nb_players, nb_civs)
  - send_dm(user, content)
  - send_embed_dm(user, embed)
  - emote_from_id(id)
  - leader_from_id(id)
  - trim(str)
  - is_n_in_list(id, liste)
* **mapvote.py**
  - make_mapvote
  - make_generic_mapvote
* **ranked.py**
  - valid_report(liste_players)
  - display_scoreboard
  - setup_scoreboard(channel)
  - parsed_rank(n)
  - parsed_skill(skill)
  - parsed_wins(wins)
  - parsed_lost(lost)
  - parsed_top1(top1)
  - parsed_winrate(winrate)
  - get_games_played(user)
  - get_elo(user)
  - get_top1(user)
  - get_wins(user)
  - get_lost(user)
  - get_date(user)
  - add_user(user)
  - update_elo(user, new_elo)
  - update_top1(user)
  - update_wins(user)
  - update_lost(user)
  - update_date(user)
  - is_player_in_database(user)
  - is_in_list(user, liste)
