import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands
from grpc import Channel
from sympy import limit

class Greeting(commands.Cog):
    
    def __init__(self , bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self): 
        print("Bisi is ready!") 
    
    @commands.command()
    async def ping (self , ctx):
        await ctx.send('Pong!')
        
    @commands.command()
    async def hi(self,ctx):
        await ctx.send(f"Hey, {ctx.author.name} , my name is Bisi.")
        
    @commands.command()
    async def source(self , ctx):
        await ctx.send(f"Hello {ctx.author.name} {os.linesep}https://github.com/Imnaseli/Bisi")

    
def setup (bot):
    bot.add_cog(Greeting(bot))