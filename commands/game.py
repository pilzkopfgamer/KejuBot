import discord
from discord.ext import commands
from discord_slash import cog_ext


class game(commands.Cog):
    def __init__(self, client):
        self.client=client

    @cog_ext.cog_slash(name="game", description="Dies ist ein game!")
    async def game(self, ctx):
      embed = discord.Embed(title="Game", description=("Game wurde gestartet"),
                              color=0xe91e63)
      embed.set_footer(text='Copyright | Made by Keju Coding Team')
      await ctx.send(embed=embed)
      embed = discord.Embed(title="Game", description="**Comming Soon**", color=0xe91e63)
      embed.set_footer(text='Copyright | Made by Keju Coding Team')
      await ctx.send(embed=embed)


def setup(client):
  client.add_cog(game(client))