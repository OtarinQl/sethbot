#Thunderbot v.1.2.3 20/1/2019
import os
from func import twitter, housamo
from discord.ext import commands
import dnd

bot = commands.Bot(command_prefix = '-')

@bot.event
async def on_ready():
    print('El bot está conectado.')

@bot.event
async def on_message(msg):

    if msg.content.startswith('-hello'):
        await msg.channel.send('Hello, **BABY**')
    if msg.content.startswith('-t'):
        await msg.channel.send(twitter(msg.content.split(' ')[1]))
    if msg.content.startswith('-h'):
        if len(msg.content.split(' '))==2:
            x = housamo(msg.content.split(' ')[1])
        else:
            x = housamo(msg.content.split(' ')[1],msg.content.split(' ')[2])
        if x[0]:
            await msg.channel.send(embed=x[1])
        else:
            await msg.channel.send(x[1])

    if msg.content.startswith('-dice'):
        arguments = msg.content.split(" ")
        results = dnd.throw_dice(arguments[1])
        await msg.channel.send('Los dados rollearon: ' + ', '.join(map(lambda x0: str(x0), results)))
        pass

bot.run(os.getenv('Token'))
