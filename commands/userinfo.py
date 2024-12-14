import discord
from discord.ext import commands
from discord_slash import cog_ext

class userinfo(commands.Cog):
  def __init__(self, client):
    self.client=client

  @cog_ext.cog_slash(name="userinfo", description=
    "Mit diesem Befehl zeigst du dir die Userinfo von Useren auf dem Server an"
)
  async def userinfo(self, ctx, member: discord.Member = None):
      if member == None:
          embed = discord.Embed(title=f"Userinfo für {ctx.author.display_name}",
                              color=0xff0000)
          embed.add_field(name="Name", value=f"```{ctx.author}```")
          embed.add_field(name="Status:", value=f"```{ctx.author.status}```")
          embed.add_field(name="Bot:",
                        value=f'```{("Ja" if ctx.author.bot else "Nein")}```')
          embed.add_field(name="Server beigetreten:",
                        value=f"```{ctx.author.joined_at}```")
          embed.add_field(name="Discord beigetreten:",
                        value=f"```{ctx.author.created_at}```")
          embed.add_field(name="Rollen:",
                        value=f"```{len(ctx.author.roles) - 1}```")
          embed.set_footer(text='Copyright | Made by Keju_Bot Coding Team')
          await ctx.send(embed=embed)
      else:
          embed = discord.Embed(title=f"Userinfo für {member.display_name}",
                              color=0xff0000)
          embed.add_field(name="Name", value=f"```{member}```")
          embed.add_field(name="Status:", value=f"```{member.status}```")
          embed.add_field(name="Bot:",
                        value=f'```{("Ja" if member.bot else "Nein")}```')
          embed.add_field(name="Server beigetreten:",
                        value=f"```{member.joined_at}```")
          embed.add_field(name="Discord beigetreten:",
                        value=f"```{member.created_at}```")
          embed.add_field(name="Rollen:", value=f"```{len(member.roles) - 1}```")
          embed.set_footer(text='Copyright | Made by Keju Coding Team')
          await ctx.send(embed=embed)