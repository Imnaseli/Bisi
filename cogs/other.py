import discord
import aiohttp
import os
import asyncio
import random 
from discord.ext import commands
from grpc import Channel
from sympy import limit


class Other(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def meme(self , ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed = embed)
    
    @commands.command()
    async def thanks(self , ctx):
        await ctx.send(f"You are welcome, {ctx.author.name}")

    @commands.command()
    async def about(self , ctx):
        await ctx.send("I am an all-mighty Intelligent Discord server bot built by Oluwasijibomi Ilesanmi")

    @commands.command()
    async def badgirl( self , ctx):
        await ctx.send(f"I'm soo sorry {ctx.author.name}, please spank me sir")
    
    @commands.command()
    async def bitch(self , ctx):
        await ctx.send(f"Yes sir, what do you need?")

    @commands.command()
    async def creator(self , ctx):
        await ctx.send("https://github.com/Imnaseli")
    
def setup (bot):
    bot.add_cog(Other(bot))