import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands , tasks
from grpc import Channel
from sympy import limit
from config import *

class Random(commands.Cog):
    
    def __init__(self , bot  ):
        self.bot = bot 
        self.randtips = tips
        
    @commands.command(help="/ Ask Bisi for some life tips" , aliases = ['tips' , 'Tips' , 'TIPS' , 'tipp' , 'Tip'])
    async def tip(self ,ctx ):
        choice = random.randint(0,len(tips))
        await ctx.send(tips[choice])
        


def setup (bot):
    bot.add_cog(Random(bot))