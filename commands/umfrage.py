import discord
from discord.ext import commands
from discord_slash import cog_ext

class umfrage(commands.Cog):
    def __init__(self, client):
        self.client=client

    @cog_ext.cog_slash(name="Umfrage", description="Mache eine Umfrage")
    async def abstimmung(self, ctx,*,message):
      if ctx.author.permissions_in(ctx.channel).ban_members:
          emb=discord.Embed(title="Umfrage", description=f"{message}")
          msg=await ctx.channel.send(embed=emb)
          await msg.add_reaction('👍')
          await msg.add_reaction('👎')
      else:
        await ctx.send("**Dafür hast du keine Berechtigung!**")


def setup(client):
  client.add_cog(umfrage(client))