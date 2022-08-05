import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands , tasks
from grpc import Channel
from sqlalchemy import alias
from sympy import limit
from config import *

class Greeting(commands.Cog):
    
    def __init__(self , bot):
        self.bot = bot
        self.counter = 0
        self.tips = tips
    
    @commands.command(help="/ Call Bisi up" , aliases = ['bis','BISI','BIS','BSI','Bis','Bisii'])
    async def bisi(self,ctx):
        await ctx.send(f"Hello {ctx.author.name} , i love my name too.")
        # self.counter =+ 1
        # if (self.counter % 2 == 0):
        #     # await asyncio.sleep(1)
        #     await ctx.send(random.choice(self.tips))
        
    @commands.command(help="/ Call Bisi up" , aliases = ['hey', 'hello' ,'hii','hiii' , 'hy','hyy','yoo','yo','heyy'])
    async def hi(self,ctx):
        await ctx.send(f"Hey {ctx.author.name} , my name is Bisi.")
        


def setup (bot):
    bot.add_cog(Greeting(bot))