import discord
from discord.ext import commands
from discord_slash import cog_ext

class ban(commands.Cog):
    def __init__(self, client):
        self.client=client

    @cog_ext.cog_slash(name="ban", description="Banne einen spieler")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
      guild = ctx.guild
      if ctx.author.permissions_in(ctx.channel).ban_members:
        await ctx.guild.ban(member)
        await ctx.send(f"Du hast **{member.name}** erfolgreich für **{reason}** gebannt!")
        await member.send(f"Du bist auf {guild.name} für {reason} gebannt")
      else:
        await ctx.send("**Dafür hast du keine Berechtigung!**")


def setup(client):
  client.add_cog(ban(client))