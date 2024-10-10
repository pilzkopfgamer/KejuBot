import json
import os
import discord
import asyncio
import random

from discord_slash import SlashCommand
from discord.ext import commands
from keep_alive import keep_alive
####################Config#############################################

#####################Bot und Slash########################################

client = commands.Bot(command_prefix=".",intents=discord.Intents.all())
slash=SlashCommand(client, sync_commands=True)
##########################Cogs/Commands###################################

for filename in os.listdir("./commands"):
  if filename.endswith(".py"):
    client.load_extension(f"commands.{filename[:-3]}")

####################BotBeschreibung#######################################

@client.event
async def on_ready():
    print("Hallo Welt")
    await client.change_presence(activity=discord.Game("Was ist der Lieblings Snack von Autos? -- Parkplätzchen "),status=discord.Status.online)


####################Event für self roles###################################


@client.event
async def on_raw_reaction_add(payload):

    if payload.member.bot:
        pass

    else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['message_id'] == payload.message_id:  
                    if x['emoji'] == payload.emoji.name:  
                        role = discord.utils.get(client.get_guild(
                            payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):

    with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:

            if x['message_id'] == payload.message_id:  
                if x['emoji'] == payload.emoji.name:  
                    role = discord.utils.get(client.get_guild(
                        payload.guild_id).roles, id=x['role_id'])

                
                await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

              
########################Musik################################################

client.lavalink_nodes = [
    {"host": "lava.link", "port": 80, "password": "dismusic"},
]
client.spotify_credentials = {
    'client_id': 'bc16d29533104f44bfece3c01d364865',
    'client_secret': '5e1d2b1e4ca24e55b3014521915e1cec'
}

#######################Client.run#############################################


client.load_extension('dismusic')
keep_alive()
client.run("MTA5ODk4MjcxMjEwNDE5ODIxNg.G8zxN8.Y9G-K7iciCYySDAGjecwBOS3JFdgagmY2KyxDY")
