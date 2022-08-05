import discord
from discord.ext import commands
from grpc import Channel
from sympy import limit
from config import *

class Moderation(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.has_permissions(administrator = True)
    @commands.command(help="/ Clear previous messages, specify number of messages")
    async def clear(self ,ctx , amount = 5):
        await ctx.channel.purge(limit = amount)
        # await ctx.send("Done!")
    
    @commands.has_permissions(administrator = True)
    @commands.command(help="/ Kick member out, specify reason")
    async def kick (self ,ctx ,member : discord.Member , * , reason = None):
        await member.kick(reason = reason)
        await ctx.send(f"{member.mention} has been kicked ({reason})")
    
    @commands.has_permissions(administrator = True)
    @commands.command(help="/ Ban member, specify reason")
    async def ban (self ,ctx , member : discord.Member , * , reason = None):
        await member.ban(reason = reason)
        await ctx.send(f"{member.mention} has been banned ({reason})")
        
    @commands.has_permissions(administrator = True)
    @commands.command(help="/ Find out who created Bisi")
    async def unban(self ,ctx , * , member):
        bannedUsers = await ctx.guild.bans()
        member_name , member_discriminator = member.split('#')
        
        #loops through the list of banned users in DB (bannedUsers = await ctx.guild.bans)
        for banMember in bannedUsers:
            user = banMember.user
            
            #if the name and discriminator was found in the list then unba him/her/they from the list 
            if (user.name , user.discriminator) == (member_name , member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send (f"Unbanned {user.name} with discriminator #{user.discriminator}")
                return


def setup (bot):
    bot.add_cog(Moderation(bot))