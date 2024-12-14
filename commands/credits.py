import discord
from discord.ext import commands
from discord_slash import cog_ext

class test(commands.Cog):
    def __init__(self, client):
        self.client=client

    @cog_ext.cog_slash(name="credits", description="Zeigt dir Credits an")
    async def test(self, ctx):
      embed = discord.Embed(title="Credits", description="Der Bot wurde von Samy#7410 und Pilzkopfgamer#3375 gecodet aka Keju Coding Team")
      embed.set_footer(text="Copyrigt | Made by Keju Coding Team")
      await ctx.send(embed=embed)


def setup(client):
  client.add_cog(test(client))