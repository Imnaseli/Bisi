import discord
from discord.ext import commands
from config import *

TOKEN_ = Discord_key
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bisi is ready!")

client.run(TOKEN)
# print(TOKEN)