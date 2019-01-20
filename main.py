#Thunderbot v.1.2.3 20/1/2019
import os
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
        if len(msg.content.split(' '))==2:
            x = housamo(msg.content.split(' ')[1])
        else:
            x = housamo(msg.content.split(' ')[1],msg.content.split(' ')[2])
        if x[0]:
            await bot.send_message(channel, embed=x[1])
        else:
            await bot.send_message(channel,x[1])

bot.run(os.getenv('Token'))
