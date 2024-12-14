import discord
from discord.ext import commands
from discord_slash import cog_ext

class version(commands.Cog):
  def __init__(self, client):
    self.client=client

  @cog_ext.cog_slash(name="Version", description="Zeigt dir die Version des Bots   an und der Befehle")
  async def userinfo(self, ctx):
      embed = discord.Embed(title="Command Versionen",description=
                           "Userinfo Version **1.0.0**\r\n"
                           "\r\nMute Version Beta **1.0.0**\r\n"
                           "\r\nGame Version Preview **0.0.1**\r\n"
                           "\r\nBan Version Alpha **1.0.0**\r\n"
                           "\r\nAnnouncement Version **1.0.0**")
      embed.set_footer(text='Copyright | Made by Keju Coding Team')
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(version(client))