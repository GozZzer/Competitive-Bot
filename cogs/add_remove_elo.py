import json
import jmespath
import discord
from discord.ext import commands


# create the class/cog
class staff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, member: discord.Member, amount=int(0)):
        permission = False

        if 'staff' in str(ctx.author.roles).lower():
            permission = True
        if permission is True:

            # safe in json file
            id = str(member.id)
            with open("elo.json") as f:
                datas = json.load(f)

            while True:
                try:
                    felo = datas[id]["elo"]
                    break
                except:
                    datas.setdefault(id, {})
                    datas[id]["elo"] = 0
                    datas[id]["rank"] = "Coal"
                    with open('elo.json', 'w') as f:
                        json.dump(datas, f, indent=4)
                    felo = 0
                    break

            elo = felo + amount

            with open("elo.json") as f:
                data = json.load(f)

            rank = ""
            if elo < 0:
                elo = 0
                rank = "Coal"
            elif 0 <= elo < 100:
                rank = "Coal"
            elif 100 <= elo < 200:
                rank = "Iron"
            elif 200 <= elo < 300:
                rank = "Gold"
            elif 300 <= elo < 400:
                rank = "Diamond"
            elif 400 <= elo < 500:
                rank = "Emerald"
            elif 500 <= elo < 600:
                rank = "Sapphire"
            elif elo >= 600:
                rank = "Ruby"

            datas.setdefault(id, {})
            data[id]["elo"] = elo
            data[id]["rank"] = rank

            with open('elo.json', 'w') as f:
                json.dump(data, f, indent=4)

            await ctx.send(f'Added **{str(amount)}** Elo to {member.mention}')

        else:
            await ctx.send('You are not allowed to add Elo!!')

    @commands.command()
    async def rem(self, ctx, member: discord.Member, amount=int(0)):
        permission = False

        if 'staff' in str(ctx.author.roles).lower():
            permission = True
        if permission is True:

            # safe in json file
            id = str(member.id)
            with open("elo.json") as f:
                datas = json.load(f)


            while True:
                try:
                    felo = datas[id]["elo"]
                    break
                except:
                    datas.setdefault(id, {})
                    datas[id]["elo"] = 0
                    datas[id]["rank"] = "Coal"
                    with open('elo.json', 'w') as f:
                        json.dump(datas, f, indent=4)
                    felo = 0
                    break

            elo = felo - amount

            with open("elo.json") as f:
                data = json.load(f)

            rank = ""
            if elo < 0:
                elo = 0
                rank = "Coal"
            elif 0 <= elo < 100:
                rank = "Coal"
            elif 100 <= elo < 200:
                rank = "Iron"
            elif 200 <= elo < 300:
                rank = "Gold"
            elif 300 <= elo < 400:
                rank = "Diamond"
            elif 400 <= elo < 500:
                rank = "Emerald"
            elif 500 <= elo < 600:
                rank = "Sapphire"
            elif elo >= 600:
                rank = "Ruby"

            datas.setdefault(id, {})
            data[id]["elo"] = elo
            data[id]["rank"] = rank

            with open('elo.json', 'w') as f:
                json.dump(data, f, indent=4)

            await ctx.send(f'Removed **{str(amount)}** Elo from {member.mention}')

        else:
            await ctx.send('You are not allowed to remove Elo!!')


# setup function
def setup(client):
    client.add_cog(staff(client))
