#Thunderbot v.1.1.3 8/12/2018
import re
import os
import discord
import asyncio
from discord.ext import commands
from requests_html import HTMLSession

def housamo(y):
    session = HTMLSession()
    r = session.get('https://wiki.housamo.xyz/'+y[1].capitalize())
    if(str(r)!='<Response [404]>'):
        if(len(y)==2 or y[2]=='3'):
            htmlCd = r.html.find('#transient0',first=True)
            x = 0
        else:
            tabla = r.html.find('.toc',first=True)
            tb = re.findall('☆\d|Variant',tabla.text)
            x = 0
            while('☆'+y[2]!=tb[x]):
                x = x+1
            htmlCd = r.html.find('#transient'+str(x),first=True)
        urls = r.html.search_all('<img src=\"{}\"')
        if not re.match('.+\.png.+',str(urls[0])):
            urls = r.html.search_all('<img alt=\"{}\" src=\"{}\"')
        icon = []
        icon.append(re.findall('https://.+\.png',str(urls[x*2]))[0])
        icon.append(re.findall('https://.+\.png',str(urls[(x*2)+1]))[0])
        match = re.findall('setTimeout.+',str(htmlCd.text))
        if(len(match)>0):
            info = htmlCd.text.replace(match[0],'')
        else:
            info = htmlCd.text
        return [[y[1].capitalize(), info, icon],True]
    else:
        return ['No existe nada sobre `'+y[1]+'` :thinking:\nPrueba mandando el mensaje otra vez', False]

def twitter(x):
    session = HTMLSession()
    r = session.get(x)
    img = r.html.search_all('data-image-url=\"{}\"')
    x = 0
    mens = ''
    while x<4:
        mens = mens + str(img[x].fixed) + '\n'
        x=x+1
    for char in '(\',)':
        mens = mens.replace(char,'')
    return mens

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('El bot está conectado.')

@client.event
async def on_message(msg):
    
    chn = msg.channel
    
    if (msg.content.startswith('https://twitter.com/')):
        rec = str(msg.content).split(' ')
        x = twitter(rec[0])
        await client.send_message(chn, x)
    
    if (msg.content.startswith('-h')):
        rec = str(msg.content).split(' ')
        x = housamo(rec)
        if(x[1]):
            y = x[0]
            embed = discord.Embed(title=y[0], description=y[1], color=0x00ff00)
            embed.set_footer(text=y[0],icon_url=y[2][0])
            embed.set_image(url=y[2][1])
            await client.send_message(chn, embed=embed)
        else:
            await client.send_message(chn,x[0])

client.run(os.getenv('Token'))
