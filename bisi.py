import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands
from grpc import Channel
from sympy import limit
from config import *
"""""
An Event is a piece of code that runs when the bot detects that a specific activity has happened(Line)
The prefix is the character we put before our command that make the bot run it (Line)
Event decorator / simply saying " eyo! this is an Event "

"""""
Discord_key = TOKEN_ 
bot = commands.Bot(command_prefix='.')

@bot.event 
async def on_ready(): 
    print("Bisi is ready!") #Of course you are
    
@bot.event
async def on_member_join(member):
    print(f"{member} has joined The Shifty Hell server.")
    
@bot.event
async def on_member_remove(member):
    print(f"{member} has left The Shifty Hell server.")
    
@bot.command()
async def hi(ctx):
    await ctx.send(f"Hey, {ctx.author.name} , my name is Bisi.")

@bot.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
    
@bot.command()
async def thanks(ctx):
    await ctx.send(f"You are welcome, {ctx.author.name}")

@bot.command()
async def badgirl(ctx):
    await ctx.send(f"I'm soo sorry {ctx.author.name}, please spank me sir")
    
@bot.command()
async def bitch(ctx):
    await ctx.send(f"Yes sir, what do you need?")

@bot.command()
async def source(ctx):
    await ctx.send(f"Hello {ctx.author.name} {os.linesep}https://github.com/Imnaseli/Bisi")

@bot.command()
async def about(ctx):
    await ctx.send("I am an all-mighty Intelligent Discord server bot built by Oluwasijibomi Ilesanmi")
    
    


bot.run(Discord_key) #The bot instance has to run right?
