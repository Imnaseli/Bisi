import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands , tasks
from grpc import Channel
from sympy import limit
"""""
An Event is a piece of code that runs when the bot detects that a specific activity has happened(Line)
The prefix is the character we put before our command that make the bot run it (Line)
Event decorator / simply saying " eyo! this is an Event "

"""""
from config import *
Discord_key = TOKEN_ 
bot = commands.Bot(command_prefix='.')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
    change_status.start()
    await bot.change_presence(status=discord.Status.online) 
    print("Bisi is ready!")
    
@tasks.loop(minutes=2.5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(statuses)))

@commands.has_permissions(administrator = True)
@bot.command(help = "/ For Administrators")
async def load(ctx , extension):
    bot.load_extension(f'cogs.{extension}')

@commands.has_permissions(administrator = True)
@bot.command(help = "/ For Administrators")
async def unload(ctx , extension):
    bot.unload_extension(f'cogs.{extension}')

@commands.has_permissions(administrator = True)    
@bot.command(help = "/ For Administrators" , aliases = ['rel' , 'relo' , 'rl' ,'r'])
async def reload(ctx , extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Errors - For now will create a cog for it soon.
@bot.event
async def on_command_error (ctx , error):
    if isinstance(error , commands.CommandNotFound):
        await ctx.send(f"Invalid command from {ctx.author.name}{os.linesep}(Please use .help to see a list of all commands)")







#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(Discord_key) #The bot instance has to run right?
