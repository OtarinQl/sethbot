# Thunderbot v.2.0 20/06/2019
# Te quiero Ota~
import os
from func import twitter, housamo
import discord
from discord.ext import commands
import dnd
import firebase
import instrumentality as instr

bot = commands.Bot(command_prefix='-', description='Eating ass')


@bot.event
async def on_ready():
    print('El bot está conectado.')
    await bot.change_presence(activity=discord.Game(name='with himself'))


@bot.command()
async def test(ctx, var1, var2='Nepe'):
    print(str(ctx))
    print(var1)
    print(var2)
    await ctx.send('Tested')


@bot.command()
async def hello(ctx):
    await ctx.send('Hello, **BABY**')


@bot.command()
async def update_user_info(ctx):
    instrumentality.update_server_user_info()
    await ctx.send('Todavia no implemento esto Dingo, **BABY**')


@bot.command()
async def t(ctx, link):
    await ctx.send(twitter(link))


@bot.command()
async def h(ctx, husbando, rarity=3):
    await ctx.send(housamo(husbando, rarity))


@bot.group()
async def inv(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Tenes que pasarme algun comando con eso...**BABY**')


@inv.command()
async def add(ctx,  *, item):
    dnd.add_to_inventory(ctx.message.author, item)
    await ctx.send('Se ha añadido un ' + item + ' al inventario, **BABY**')


@inv.command()
async def show(ctx):
    result = dnd.show_inventory(ctx.message.author)
    await ctx.send('Inventario: \n' + '\n '.join(result))


@inv.command()
async def delete(ctx, *, item):
    result = dnd.delete_from_inventory(ctx.message.author, item)
    await ctx.send(result)


@bot.command()
async def dice(ctx, die):
    results = dnd.throw_dice(die)
    await ctx.send('Los dados rollearon: ' + ', '.join(map(lambda x0: str(x0), results)))


@bot.group()
async def instrumentality(ctx):
    if ctx.invoked_subcommand is None:
        if instr.is_user_opted_in(ctx.message.author):
            await ctx.send('Estas metido en el proyecto de instrumentalidad humana, **BABY**')
        else:
            await ctx.send('No estas en el proyecto de instrumentalidad humana, **BABY**')


@instrumentality.command()
async def opt_in(ctx):
    instr.opt_in(ctx.message.author)
    await ctx.send("Acabas de entrar al programa de instrumentalidad humana, **BABY**")


@instrumentality.command()
async def opt_out(ctx):
    instr.opt_out(ctx.message.author)
    await ctx.send("Acabas de salir del programa de instrumentalidad humana, **BABY**")


@bot.event
async def on_message(msg):
    if not msg.author.bot and instr.is_user_opted_in(msg.author):
        instr.store_message(msg)

    await bot.process_commands(msg)

# Production
token = os.getenv('Token')

# Local
if token == None:
    with open("token.txt", "r") as token_file:
        token = token_file.readline()

bot.run(token)
