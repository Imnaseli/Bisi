import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands , tasks
from grpc import Channel
from sympy import limit
from config import *

class Emojis(commands.Cog):
    
    def __init__(self , bot  ):
        self.bot = bot
        
    @commands.command()
    async def lol (self ,ctx):
        await ctx.send("🤣🤣🤣")

        
        
        
        
        
        
def setup (bot):
    bot.add_cog(Emojis(bot))