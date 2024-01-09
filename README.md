# Civ-Private-Bot
Civ Private Bot is a discord bot created to help on Civ Private Club.
This bot is hosted by Adkynet SAS.

Prefix : '$'

Files summary :
  - README.md : your are actualy reading this file
  - main.py : core of the bot. Where commands are defined
  - birthdays.py : contains all the needed functions managing birthdays
  - db.sqlite : database (contains 2 tables : Anniversaires (for birthdays), Ranked (for future ranking system))
  - pyenv.cfg : config
  - requirements.txt : names of the needed libraries (file not needed to run localy)

List of the supported commands :
  - $hello(ctx) : introduce itself
  - $serverinfo(ctx) : give informations about the server
  - $clear(ctx, n) : clear the n latest messages of the channel
  - $mapvote(ctx) : launch a mapvote for Civilization VI
  - $set_birthday(ctx, date) : add/modify your birthday in the database
  - $birthdays : display birthdays from database

List of ideas to add :
  - A ranking system
  - Upgrade mapvote() command (more like CivFR/CPL)
  - make_team() (based on players ranking in database)
  - Triggers to wish happy birthday
  - Improve the UI for birthdays (embed, sorted by months, ...)
