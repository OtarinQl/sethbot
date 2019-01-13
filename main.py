#Thunderbot v.1.2.1 13/1/2019
import os
import discord
from func import twitter, housamo
from discord.ext import commands

bot = commands.Bot(command_prefix = '-')

@bot.event
async def on_ready():
    print('El bot está conectado.')

@bot.event
async def on_message(msg):
    channel = msg.channel
    if msg.content.startswith('-t'):
        await bot.send_message(channel, twitter(msg.content.split(' ')[1]))
    if msg.content.startswith('-h'):
        x = housamo(msg.content.split(' ')[1])
        if x[0]:
            cont = discord.Embed(title=msg.content.split(' ')[1].capitalize(), description=x[1], color=0x00ff00)
            cont.set_image(url=x[2])
            cont.set_footer(text=msg.content.split(' ')[1].capitalize(), icon_url=x[3])
            await bot.send_message(channel, embed=cont)
        else:
            await bot.send_message(channel,x[1])

bot.run(os.getenv('Token'))
