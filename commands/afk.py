import discord
from discord.ext import commands
from discord_slash import cog_ext

class afk(commands.Cog):
    def __init__(self, client):
        self.client=client

    @cog_ext.cog_slash(name="Afk", description="Stelle dich Afk")
    async def afk(ctx, *, reason):
        await ctx.send(f"**{ctx.author}** ist nun wegen **{reason}** AFK")
        


def setup(client):
  client.add_cog(afk(client))