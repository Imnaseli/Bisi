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
        
    @commands.command(help="/ Ask Bisi for some facts" , aliases = ['tips' , 'Tips' , 'TIPS' , 'tipp' , 'Tip'])
    async def tip(self ,ctx ):
        choice = random.randint(0,len(tips)+1)
        await ctx.send(tips[choice])
    
    @commands.command(help="/ Random Number", aliases = ['rand' , 'rando' , 'Randomnumber' ] )
    async def randomnumber(self ,ctx , *,number  = 100 ):
        choice = random.randint(0,number)
        await ctx.send(choice)
        
#, aliases = ['rand' , 'rando' , 'Randomnumber' ]

def setup (bot):
    bot.add_cog(Random(bot))