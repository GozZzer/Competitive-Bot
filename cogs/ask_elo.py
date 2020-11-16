import discord
import json
from discord.ext import commands


# create the class/cog
class user(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx, member: discord.Member = None):
        if member is None:
            id = str(ctx.author.id)
            name = str(ctx.author)
        else:
            id = str(member.id)
            name = str(member)
        with open("elo.json") as f:
            data = json.load(f)
        name = name[:-5]

        while True:
            try:
                elo = data[id]["elo"]
                rank = data[id]["rank"]
                embed = discord.Embed(title=f'{name}`s Elo Info', color=00000)
                embed.add_field(name="Rank:", value=rank, inline=True)
                embed.add_field(name="Elo:", value=elo, inline=True)
                await ctx.send(embed=embed)
                break
            except:
                await ctx.send(f'{name} has no Elo.')
                await ctx.send('**Staff** has to add/remove Elo before you can use this command.')
                break

    @commands.command()
    async def top(self, ctx):
        embedtop = discord.Embed(title='Top10', description='Will be updated every 24 hours at 8pm(UTC).', color=00000)
        embedtop.add_field(name='#1', value='[Rank] [Name] [Elo]Elo', inline=False)
        embedtop.add_field(name='#2', value='[Rank] [Name] [Elo]Elo', inline=False)
        embedtop.add_field(name='#3', value='[Rank] [Name] [Elo]Elo', inline=False)
        embedtop.add_field(name='#4', value='[Rank] [Name] [Elo]Elo', inline=False)
        embedtop.add_field(name='#5', value='[Rank] [Name] [Elo]Elo', inline=False)
        embedtop.add_field(name='#6', value='[Rank] [Name] [Elo]Elo', inline=False)
        embedtop.add_field(name='#7', value='[Rank] [Name] [Elo]Elo', inline=False)
        embedtop.add_field(name='#8', value='[Rank] [Name] [Elo]Elo', inline=False)
        embedtop.add_field(name='#9', value='[Rank] [Name] [Elo]Elo', inline=False)
        embedtop.add_field(name='#10', value='[Rank] [Name] [Elo]Elo', inline=False)
        embedtop.set_footer(text='Updated: [Date] 8pm Timezone: UTC')
        await ctx.send(embed=embedtop)

    @commands.command()
    async def ranks(self, ctx):
        embedr = discord.Embed(title="Ranks", color=00000)
        embedr.add_field(name="Coal", value="0 - 99 Elo", inline=False)
        embedr.add_field(name="Iron", value="100 - 199 Elo", inline=False)
        embedr.add_field(name="Gold", value="200 - 299 Elo", inline=False)
        embedr.add_field(name="Diamond", value="300 - 399 Elo", inline=False)
        embedr.add_field(name="Emerald", value="400 - 499 Elo", inline=False)
        embedr.add_field(name="Sapphire", value="500 - 599 Elo", inline=False)
        embedr.add_field(name="Ruby", value="600+ Elo", inline=False)
        await ctx.send(embed=embedr)


# setup function
def setup(client):
    client.add_cog(user(client))
