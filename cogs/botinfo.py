import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands , tasks
from grpc import Channel
from sympy import limit
from config import *

class Main(commands.Cog):
    
    def __init__(self , bot):
        self.bot = bot
        self.randaboutbisi = aboutbisi
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     await self.send_to_all('Bisi is Online!')
        
    @commands.command(help="/ Find out who created Bisi")
    async def creator(self , ctx):
        await ctx.send("My creator is a genius https://github.com/Imnaseli")

    @commands.command(help="/ How was Bisi made?")
    async def source(self , ctx):
        await ctx.send(f"Hello {ctx.author.name} {os.linesep}https://github.com/Imnaseli/Bisi")
        
    @commands.command(help="/ Find out who Bisi is")
    async def about(self , ctx):
        await ctx.send(next(self.randaboutbisi))
    
def setup (bot):
    bot.add_cog(Main(bot))