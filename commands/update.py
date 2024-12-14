import discord
from discord.ext import commands
from discord_slash import cog_ext

class update(commands.Cog):
    def __init__(self, client):
        self.client=client

    @cog_ext.cog_slash(name="Update", description="Zeigt dir die Update Notes an")
    async def update(self, ctx):
      embed = discord.Embed(title="Update Notes 📝", description="**Update Version 0.0.1**\r\n"
                           "**-**Game Command\r\n"
                           "**-**ban command private Nachricht überarbeiten\r\n"
                           "**-**Alle Commands ein bisschen überarbeiten")
      embed.set_footer(text='Copyright | Made by Keju Coding Team')
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(update(client))