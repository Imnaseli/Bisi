import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands , tasks
from grpc import Channel
from sympy import limit


class Welcome(commands.Cog):
    def __init__(self , bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, ctx , member):
        await ctx.send(f"{member} has joined The Shifty Hell.")
        print(f"{member} has joined The Shifty Hell server.")
        
    @commands.Cog.listener()
    async def on_member_remove(self , ctx,member):
        await ctx.send(f"{member} has left The Shifty Hell.")
        print(f"{member} has left The Shifty Hell server.")
    
    
        
def setup (bot):
    bot.add_cog(Welcome(bot))