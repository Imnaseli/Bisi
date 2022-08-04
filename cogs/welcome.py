import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands
from grpc import Channel
from sympy import limit


class Welcome(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self , member):
        print(f"{member} has joined The Shifty Hell server.")
        
    @commands.Cog.listener()
    async def on_member_remove(self , member):
        print(f"{member} has left The Shifty Hell server.")
    
    @commands.command()
    async def fetch(self,ctx):
        await ctx.send(f"Hey, {ctx.author.name} , my name is Bisi.")
        
def setup (bot):
    bot.add_cog(Welcome(bot))