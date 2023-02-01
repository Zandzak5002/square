from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions#
import random
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class flip(commands.Cog, name="Flip"):
  """flip a coin"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Flip a coin.")
  @commands.guild_only()
  async def flip(self, ctx):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["dadjoke"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The rps command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["fun"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The fun module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
      try:
        optionchoosed = random.choice(["heads", "tails"])
        return await ctx.respond(f'{ctx.author.mention} {optionchoosed}')
      except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)  


def setup(bot: commands.Bot):
  
  bot.add_cog(flip(bot))