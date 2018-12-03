#Sethbot v.1.1.0 2/12/2018
import re
import os
import discord
import asyncio
from discord.ext import commands
from requests_html import HTMLSession

def twitter(x):
    session = HTMLSession()
    r = session.get(x)
    img = r.html.find('.AdaptiveMedia-container', first=True)
    htmlCd = img.html
    src = re.findall('https://.+\.jpg|https://.+\.png', htmlCd)
    list = ''
    if (len(src) > 2):
        for x in range(0, (len(src) - 1)):
            if (x % 2 == 0 and x > 1):
                list = list + src[x] + '\n'
    else:
        list = 'No hay imagen qué agregar tho :thinking:'
    return list

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('El bot está conectado.')

@client.event
async def on_message(msg):
    chn = msg.channel

    if (msg.content.startswith('-t')):
        rec = str(msg.content).split(' ')
        x = twitter(rec[1])
        await client.send_message(chn, x)

client.run(os.getenv('Token'))
