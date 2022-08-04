import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands , tasks
from grpc import Channel
from sympy import limit

class Greeting(commands.Cog):
    
    def __init__(self , bot):
        self.bot = bot
    
    @commands.command(help="/ Call Bisi up")
    async def bisi(self,ctx):
        await ctx.send(f"Hello {ctx.author.name} , i love my name too.")
        
    @commands.command(help="/ Call Bisi up")
    async def hi(self,ctx):
        await ctx.send(f"Hey {ctx.author.name} , my name is Bisi.")
        


def setup (bot):
    bot.add_cog(Greeting(bot))