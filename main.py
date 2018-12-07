#Sethbot v.1.1.0 2/12/2018
import re
import os
import discord
import asyncio
from discord.ext import commands
from requests_html import HTMLSession

def housamo(y):
    session = HTMLSession()
    r = session.get('https://wiki.housamo.xyz/'+y[1])
    if(str(r)!='<Response [404]>'):
        if(len(y)==2 or y[2]=='3'):
            htmlCd = r.html.find('#transient0',first=True)
        else:
            tabla = r.html.find('.toc',first=True)
            tb = re.findall('☆\d|Variant',tabla.text)
            x = 0
            while('☆'+y[2]!=tb[x] or y[2]!=tb[x]):
                x = x+1
            htmlCd = r.html.find('#transient'+str(x),first=True)
        match = re.findall('setTimeout.+',str(htmlCd.text))
        info = htmlCd.text.replace(match[0],'')
        return [[y[1],info],True]
    else:
        return ['No existe nada sobre `'+y[1]+'` :thinking:\nPrueba mandando el mensaje otra vez', False]

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
    
    if (msg.content.startswith('Meper')):
        await client.send_message(chn, 'No.')
    
    if (msg.content.startswith('-h')):
        rec = str(msg.content).split(' ')
        x = housamo(rec)
        if(x[1]):
            y = x[0]
            embed = discord.Embed(title=y[0], description=y[1], color=0x00ff00)
            await client.send_message(chn, embed=embed)
        else:
            await client.send_message(chn,x[0])

client.run(os.getenv('Token'))
