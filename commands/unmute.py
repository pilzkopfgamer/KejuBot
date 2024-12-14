import discord
from discord.ext import commands
from discord_slash import cog_ext

class unmute(commands.Cog):
    def __init__(self, client):
        self.client=client

    @cog_ext.cog_slash(name="unmute",description="Unmute einen User")
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await ctx.send(f"{member.mention} ist entstummt")
        await member.send(f"Du bist auf {ctx.guild.name} entstummt")

def setup(client):
  client.add_cog(unmute(client))