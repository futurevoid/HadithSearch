import asyncio
import datetime as dt
from dbm import dumb
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
from keep_Alive import keep_alive

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

    elif message.content.startswith('lolhelp') or message.content.startswith('/help'):
        embed = discord.Embed(title=f"Help {message.author.mention} ".format(message), description="Here is a list of commands", color=0x00ff00)
        embed.add_field(name="lolscamalert", value="Shows scam alert meme", inline=False)
        embed.add_field(name="lolhelp", value="Displays this message", inline=False)
        await message.channel.send(embed=embed)
    elif message.content.startswith('lolscamalert') or message.content.startswith('/scamalert'):
        embed = discord.Embed(title="Scam Alert", description="", color=0x00ff00)
        embed.set_image(url="images.jpg")
        await message.channel.send(embed=embed)                                                     

vr = 'du'
vrg = vr.upper()
keep_alive()
client.run(f"OTQwMjEzMjU5NDMxMjAyODI2.YgEH1Q.tK4nzfIjr6iQjt7nND_D_1ktd{vrg}")

