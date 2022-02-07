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


bot = commands.Bot(command_prefix='^')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("0xlol") or message.content.startswith("/lol"):
        r = requests.get(
            'https://sv443.net/jokeapi/v2/joke/Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,racist,sexist&type=single').json()
        joke = r['joke']
        await message.channel.send(joke)
    elif message.content.startswith('0xtmems') or message.content.startswith('/tmems'):
         async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/TechMemes/.json?limit=100') as r:
                 res = await r.json()
                 embed = discord.Embed(title="Tech Memes", description="Here is a tech meme", color=0x00ff00)
                 embed.set_image(url=res['data']['children'][random.randint(0,99)]['data']['url'])
                 await message.channel.send(embed=embed)
    if message.content.startswith('0xmems') or message.content.startswith('/mems'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/top/.json?sort=top&t=day') as r:
                res = await r.json()
                embed = discord.Embed(title="Meme GIF", description="Here is a meme gif", color=0x00ff00)
                embed.set_image(url=res['data']['children'][random.randint(0,len(res['data']['children']))]['data']['url'])
                await message.channel.send(embed=embed)      
    elif message.content.startswith('0xgmems') or message.content.startswith('/gmems'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/gamingmemes/.json?limit=100') as r:
                res = await r.json()
                embed = discord.Embed(title="Gaming Memes", description="Here is a gaming meme", color=0x00ff00)
                embed.set_image(url=res['data']['children'][random.randint(0,99)]['data']['url'])
                await message.channel.send(embed=embed)                       