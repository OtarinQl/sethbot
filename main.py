#Thunderbot v.1.2.0 12/1/2019
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
        if x[1]:
            y=x[0]
            embed = discord.Embed(title=y[0], description=y[1], color=0x00ff00)
            embed.set_footer(text=y[0], icon_url=y[2][0])
            embed.set_image(url=y[2][1])
            await bot.send_message(channel, embed=embed)
        else:
            await bot.send_message(channel, x[0])

bot.run('NTIyNDAwNzI5NjA5MjczMzY5.DvKbuA.iKTymMqoYMKHw41xr3zyYu6eKcs')