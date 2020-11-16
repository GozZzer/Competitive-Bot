import discord
from discord.ext import commands
from variables import prefix


# create the class/cog
class helpp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Bot Help", description=f"Prefix: **{prefix}**", color=00000)
        embed.add_field(name="help", value="elo!help")
        embed.add_field(name="ranks", value="elo!ranks", inline=False)
        embed.add_field(name="info", value="elo!info [User(Only if you`ll know it from someone else)]",inline=False)
        embed.add_field(name="add", value="elo!add [User] [Elo]", inline=False)
        embed.add_field(name="rem", value="elo!rem [User] [Elo]", inline=False)

        await ctx.send(embed=embed)


# setup function
def setup(client):
    client.add_cog(helpp(client))
