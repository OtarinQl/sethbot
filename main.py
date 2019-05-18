#Thunderbot v.1.2.3 20/1/2019
import os
from func import twitter, housamo
from discord.ext import commands
import dnd
import firebase

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

    #Argumentos: 0-comando 1-seccion 2-objeto
    if msg.content.startswith('-inv'):
        arguments = msg.content.split("/")
        action = arguments[1].lower()
        if action == 'add':
            dnd.add_to_inventory(msg.author, arguments[2])
            await msg.channel.send('Se ha añadido un ' + arguments[2] + ' al inventario, **BABY**')
            pass
        elif action == "show":
            result = dnd.show_inventory(msg.author)
            await msg.channel.send('Inventario: \n' + '\n '.join(result))
            pass
        elif action == "delete":
            result = dnd.delete_from_inventory(msg.author, arguments[2])
            await msg.channel.send(result)

token = ""

# Production
# token = os.getenv('Token')

# Local
with open("token.txt", "r") as token_file:
    token = token_file.readline()

bot.run(token)
