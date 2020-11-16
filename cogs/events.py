from variables import client, commands
import discord
import asyncio


# create the class/cog
class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @client.event
    async def on_ready():
        print('Beep, Boop I am logged in.')
        while True:
            await client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="Competitive Bedwars elo!help"))

    @client.event
    async def on_command_error(self, error):
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            await self.send(f"{error}!")
            await self.send("Try **elo!help** to see all commands.")


# setup function
def setup(client):
    client.add_cog(events(client))
