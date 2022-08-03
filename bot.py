import discord
from discord.ext import commands
from config import *

Discord_key = TOKEN_ 
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bisi is ready!")

client.run(Discord_key)
