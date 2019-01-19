#Thunderbot v.1.2.2 19/1/2019
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
        if len(msg.content.split(' '))==2:
            x = housamo(msg.content.split(' ')[1])
        else:
            x = housamo(msg.content.split(' ')[1],msg.content.split(' ')[2])
        if x[0]:
            embed = discord.Embed(title=msg.content.split(' ')[1].capitalize(), color=0x00ff00)
            embed.add_field(name=x[1][0], value=x[1][1], inline=True)
            embed.add_field(name=x[2][0], value=x[2][1], inline=True)
            embed.add_field(name=x[3][0], value=x[3][1], inline=True)
            embed.add_field(name=x[4][0], value=x[4][1], inline=True)
            embed.add_field(name=x[5][0], value=x[5][1], inline=True)
            embed.add_field(name=x[6][0], value=x[6][1], inline=True)
            embed.set_image(url=x[7])
            embed.set_thumbnail(url=x[8])
            embed.set_footer(text=msg.content.split(' ')[1].capitalize(), icon_url=x[8])
            await bot.send_message(channel, embed=embed)
        else:
            await bot.send_message(channel,x[1])

bot.run(os.getenv('Token'))
