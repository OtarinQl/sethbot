#Sethbot v.1.1.0 28/11/2018
#Incluye: -mensajes en caso de que el tweet sea puramente de texto / video o en caso de que sea de una única imagen
#En futuras versiones se espera incluir: comando Housamo (h)
#A esperar comentarios para ver qué nuevas funcionalidades ingresar
import re
import discord
import asyncio
from discord.ext import commands
from requests_html import HTMLSession
#Definición de funciones

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
        list = 'No hay imagen que agregar tho :thinking:'
    return list

#Definición de token y prefijo del bot
token = 'NDgwODg5OTc5NDg1MDI4MzYy.Dtwy8g.-I5YRhHTgtFrGqif_YCVQD19R1I'
client = commands.Bot(command_prefix = '-')

#Comandos
@client.event
async def on_ready():
    print('El bot está conectado~')

@client.event
async def on_message(msg):

    chn = msg.channel

    #if (msg.content.startswith('-ayuda')):
    #   await client.send_message(chn,"""```-t [enlace de Twitter]```Manda el resto de imágenes que hay en el tweet""")

    if (msg.content.startswith('-t')):
        rec = str(msg.content).split(' ')
        x = twitter(rec[1])
        await client.send_message(chn, x)

#Inicialización del bot
client.run(token)