import discord
import os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
# token refresh needed?

client.run('MTAzOTY0NzE2NjY1NTg4OTUyOA.G2alfT.jr9VT-eJ4Jb0oi9dyRvLO3N-19wvKa1XVHT8FY')