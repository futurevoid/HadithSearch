import asyncio
import datetime as dt
import json
import os
import random
import sys
import time
from email import message
import aiohttp
import discord
#from more_itertools import sliced
import requests
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from matplotlib import image
from youtube_dl import YoutubeDL as ytdl


client = discord.Client()


# create an event that will run when the bot is ready
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


bot = commands.Bot(command_prefix='lol')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('lolTmems') or message.content.startswith('/Tmems'):
         async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/TechMemes/.json?limit=100') as r:
                 res = await r.json()
                 embed = discord.Embed(title="Tech Memes", description="Here is a tech meme", color=0x00ff00)
                 embed.set_image(url=res['data']['children'][random.randint(0,99)]['data']['url'])
                 await message.channel.send(embed=embed)
    if message.content.startswith('lolmems') or message.content.startswith('/mems'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/top/.json?sort=top&t=day') as r:
                res = await r.json()
                embed = discord.Embed(title="Meme GIF", description="Here is a meme gif", color=0x00ff00)
                embed.set_image(url=res['data']['children'][random.randint(0,len(res['data']['children']))]['data']['url'])
                await message.channel.send(embed=embed)      
    elif message.content.startswith('lol Gmems') or message.content.startswith('/gmems'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/gamingmemes/.json?limit=100') as r:
                res = await r.json()
                embed = discord.Embed(title="Gaming Memes", description="Here is a gaming meme", color=0x00ff00)
                embed.set_image(url=res['data']['children'][random.randint(0,99)]['data']['url'])
                await message.channel.send(embed=embed)
    elif message.content.startswith('lolWmems') or message.content.startswith('/wmems'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/wholesomememes/.json?limit=100') as r:
                res = await r.json()
                embed = discord.Embed(title="Wholesome Memes", description="Here is a wholesome meme", color=0x00ff00)
                embed.set_image(url=res['data']['children'][random.randint(0,99)]['data']['url'])
                await message.channel.send(embed=embed)
    elif message.content.startswith('lol help') or message.content.startswith('/help'):
        embed = discord.Embed(title="Help", description="Here is a list of commands", color=0x00ff00)
        embed.add_field(name="lolhelp", value="Displays this message", inline=False)
        embed.add_field(name="lolmems", value="Displays a meme gif", inline=False)
        embed.add_field(name="lolGmems", value="Displays a gaming meme", inline=False)
        embed.add_field(name="lolWmems", value="Displays a wholesome meme", inline=False)
        embed.add_field(name="lolTmems", value="Displays a tech meme", inline=False)
        await message.channel.send(embed=embed)                                              




