import discord
import json
from discord.ext import commands
from discord_slash import cog_ext

class reactrole(commands.Cog):
    def __init__(self, client):
        self.client=client

    @cog_ext.cog_slash(name="reactrole", description="erstelle eine Reaktions rolle")
    async def reactrole(self, ctx, emoji, role: discord.Role,*, message):
      if ctx.author.permissions_in(ctx.channel).ban_members:

        emb = discord.Embed(description=message)
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction(emoji)

        with open('reactrole.json') as json_file:
          data = json.load(json_file)

          new_react_role = {
      'role_name':role.name,
      'role_id':role.id,
      'emoji':emoji,
      'message_id':msg.id
          }

          data.append(new_react_role)

        with open('reactrole.json','w') as j:
          json.dump(data,j,indent=4)
      else:
        await ctx.send("**Dafür hast du keine Berechtigung!**")

def setup(client):
  client.add_cog(reactrole(client))