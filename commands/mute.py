import discord
from discord.ext import commands
from discord_slash import cog_ext


class mute(commands.Cog):
    def __init__(self, client):
        self.client=client

    @cog_ext.cog_slash(name="mute", description="Mute einen User")
    async def mute(ctx, member: discord.Member):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_messages=True)

        await member.add_roles(mutedRole)
        await member.send(f"Du bist auf {ctx.guild.name} gestummt")
        await ctx.send(f"{ctx.author.mention} hat {member.mention} Grass gegeben. {member.mention} hat reingebissen")


def setup(client):
  client.add_cog(mute(client))