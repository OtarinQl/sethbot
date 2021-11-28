# Thunderbot v.2.0 20/06/2019
# Te quiero Ota~
import os
from func import twitter
import discord
from discord.ext import commands
import dnd
import instrumentality as instr
import e621 as e621api
import time

bot = commands.Bot(command_prefix='-', description='Eating ass')
rp_counter = 0.0
#Estas siguientes variables habria que sacarlas del entorno y evitar numeros magicos
rp_channel = 576562538674651137 
version_text = "20/10/2019 Nazi Roller Bot Electric Boogaloo V1"

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
    # await ctx.send(housamo(husbando, rarity))
    await ctx.send('Ota no implemento esto aun, **BABY**')


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


@bot.command(name='e')
async def _promSearcher(self, ctx, limit, *, tags = ''):
    if tags:
        tags = tags.split(' ')
    else:
        tags = []
        
    try:
        Posts = e621api.getImages(tags, limit)
    except Exception as e:
        return await ctx.send(e)
    
    if Posts:
        for Post in Posts:
            EmbedMsg = discord.Embed(
                title='Publicación en 621...',
                description='Artista: {0}'.format(Post['author']),
                url='https://e621.net/posts/{0}'.format(Post['id'])
                )
                
            EmbedMsg.set_image(url= Post['url'])

            await ctx.send(embed=EmbedMsg)
    else:
        await ctx.send('La búsqueda no ha dado resultados. Pareces ser de gustos muy peculiares :woozy_face:')

@bot.command()
async def status(ctx, *, status):
    await bot.change_presence(activity=discord.Game(name=status))


@bot.command()
async def highfive(ctx):
    await ctx.send("Highfive!")
    time.sleep(1)
    await ctx.send("**SLAP**")

@bot.command()
async def version(ctx):
    global version_text
    await ctx.send(version_text)    

@bot.event
async def on_message(msg):
    await bot.process_commands(msg)
    global rp_counter
    
    if not msg.author.bot and instr.is_user_opted_in(msg.author) and not msg.content.startswith(bot.command_prefix):
        instr.store_message(msg)

    if not msg.author.bot:
        #Procesar si es un mensaje de rp aca
        if is_rp(msg) and msg.channel.id != rp_channel:
            rp_counter += 1.0
        elif rp_counter > 0:
            rp_counter -= 0.5

        if rp_counter >= 3 and rp_counter < 4:
            await msg.channel.send("**SLAP**")
            time.sleep(1)
            await msg.channel.send("Parece que alguien anda roleando afuera de #role-playing, **BABY**")
            time.sleep(1)
            await msg.channel.send("Miren que me cago en todos si no rolean donde deben, **BABY**")

        if rp_counter >= 6:
            rp_counter = 0
            await msg.channel.send("No me tienten, porque me esta doliendo el estomago... **BABY**")


def is_rp(msg):
    return msg.content.startswith('*') and msg.content.endswith('*')
    

# Production
token = os.getenv('Token')

# Local
if token == None:
    with open("token.txt", "r") as token_file:
        token = token_file.readline()

bot.run(token)
