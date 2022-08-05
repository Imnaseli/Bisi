import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands , tasks
from grpc import Channel
from sympy import limit

class Error(commands.Cog):
    
    def __init__(self , bot):
        self.bot = bot
        
        
    # @commands.Cog.listener()
    # async def on_command_error (ctx , error):
    #     if isinstance(error , commands.CommandNotFound):
    #         await ctx.send("Invalid command, pls use .help to see list of commands")
        
        



def setup (bot):
    bot.add_cog(Error(bot))