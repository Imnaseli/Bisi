import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands , tasks
from grpc import Channel
from sympy import limit


class Other(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.command(pass_context=True , help="/ Spawn random memes, this keeps the vibe going")
    async def meme(self , ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed = embed)
    
    @commands.command(help="/ Bisi deserves to be thanked sometimes.")
    async def thanks(self , ctx):
        await ctx.send(f"You are welcome, {ctx.author.name}")

    @commands.command(help = "/ Members Information")
    async def members( self , ctx):
        total = len(ctx.guild.members)
        online = len(list(filter(lambda x:  (x.status) == discord.Status.online , ctx.guild.members)))
        offline = len(list(filter(lambda x:  (x.status) == discord.Status.offline , ctx.guild.members)))
        await ctx.send(f"There are {total} people in this server {os.linesep}With {online} people online and {os.linesep} {offline} offline")
       
    @commands.command(help="/ Use this command to find out your latency")
    async def ping (self , ctx):
        await ctx.send(f'Pong! { round(self.bot.latency * 1000)}ms')
        
def setup (bot):
    bot.add_cog(Other(bot))