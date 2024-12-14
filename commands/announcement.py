import discord
from discord.ext import commands
from discord_slash import cog_ext


class announcement(commands.Cog):
    def __init__(self, client):
        self.client=client

    @cog_ext.cog_slash(name="announcement", description="Sende eine Neuigket über den Bot")
    async def announcement(self, ctx, message: discord.Message=None):
      if ctx.author.permissions_in(ctx.channel).ban_members:
        if message == None:
          await ctx.send("Bitte gebe eine Nachricht ein!")
        else:
          embed = discord.Embed(title="Neuigkeit!", description=f"{message}",
                                  coulor=discord.Colour.dark_blue())
          await ctx.send(embed=embed)
      else:
        await ctx.send("**Dafür hast du keine Berechtigung!**")

      


def setup(client):
  client.add_cog(announcement(client))