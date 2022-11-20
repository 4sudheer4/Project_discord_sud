import dislash
import discord
import os
from discord.ext import commands
import json


if os.path.exists(os.getcwd()+"/config.json"):
    with open('./config.json') as f:
        configData = json.load(f)
else:
    configTemplate = {"Token":"","prefix":"!"}

    with open(os.getcwd()+"/config.json","w+") as f:
        json.dump(configTemplate,f)

token = configData["Token"]

client = discord.Client(intents=discord.Intents.default())

intents_ = discord.Intents.default()
intents_.members = True

bot = commands.Bot(command_prefix ="!", intents = intents_)




@bot.event 
async def on_ready():
    print("bot is ready")

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(f"pong! {latency}")



# @bot.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

@bot.event
async def on_message(message):
    # to avoid sync issues between on_message and bot.command() (below line)
    await bot.process_commands(message)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# commands.Bot is a subclass of discord.Client, meaning commands.Bot inherits all of the functionality of discord.Client

# You can't really combine them because they're the same thing. commands.Bot is the extended version of discord.Client.

bot.run(token)
# client.run(token)