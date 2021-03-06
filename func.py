import discord.embeds
import requests
from bs4 import BeautifulSoup

def twitter(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text,'html.parser')
    html = soup.find(class_='AdaptiveMedia-container')
    media = html.find_all('img')
    media.pop(0)
    
    msg = ''

    if media == []:
        return 'No hay imagenes qué añadir :thinking:'
    else:
        for tag in media:
            msg = msg + str(tag.get('src')) + '\n'
        return msg
#La función de Housamo estará pausada hasta que se pueda definir nuevamente usando BS4
#def housamo(y,z = '3'):
#La función toma como entrada el nombre del personaje y lo añade al enlace de la wiki de Housamo para buscar información de este.
#    session = HTMLSession()
#    r = session.get('https://wiki.housamo.xyz/'+y.capitalize())
#    if str(r)!='<Response [404]>':
#        n = 0
#        htmlCd = r.html.find('#transient0',first=True)
#        if z.lower() != 'variant':
#            while z != str(htmlCd.search('<th>Rarity</th>\n<td>{}</td>')[0]):
#                n = n+1
#                htmlCd = r.html.find('#transient' + str(n), first=True)
#        else:
#            while htmlCd.search('<th>Variant</th>\n<td>{}</td>')==None:
#                n = n+1
#                htmlCd = r.html.find('#transient' + str(n), first=True)
#        emMes = discord.Embed(title='',color=0x00ff00)
#        rarity = ''
#        for x in range(0,int(htmlCd.search('<th>Rarity</th>\n<td>{}</td>')[0])):
#            rarity = rarity + ':star:'
#        emMes.add_field(name='Rarity',value=rarity,inline=True)
#        emMes.add_field(name='Cost',value=str(htmlCd.search('<th>Cost</th>\n<td>{}</td>')[0]),inline=True)
#        emMes.add_field(name='HP',value=str(htmlCd.search('<th>HP</th>\n<td>{}</td>')[0]),inline=True)
#        emMes.add_field(name='ATK',value=str(htmlCd.search('<th>ATK</th>\n<td>{}</td>')[0]),inline=True)
#        if str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Slash':
#            emMes.add_field(name='Weapon',value=':crossed_swords:',inline=True)
#        elif str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Blow':
#            emMes.add_field(name='Weapon', value=':boxing_glove:', inline=True)
#        elif str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Shot':
#            emMes.add_field(name='Weapon', value=':bow_and_arrow:', inline=True)
#        elif str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Snipe':
#            emMes.add_field(name='Weapon', value=':gun:', inline=True)
#        elif str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Magic':
#            emMes.add_field(name='Weapon', value=':sparkles:', inline=True)
#        elif str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Thrust':
#            emMes.add_field(name='Weapon', value=':pushpin:', inline=True)
#        type_ = ['Type','']
#        if str(htmlCd.search('class="transient-container {} transient')[0])=='all-round':
#            emMes.add_field(name='Type',value=':regional_indicator_a: :regional_indicator_l: :regional_indicator_l:',inline=True)
#        elif str(htmlCd.search('class="transient-container {} transient')[0])=='wood':
#            emMes.add_field(name='Type',value=':seedling:',inline=True)
#        elif str(htmlCd.search('class="transient-container {} transient')[0])=='fire':
#            emMes.add_field(name='Type',value=':fire:',inline=True)
#        elif str(htmlCd.search('class="transient-container {} transient')[0])=='water':
#            emMes.add_field(name='Type',value=':ocean:',inline=True)
#        elif str(htmlCd.search('class="transient-container {} transient')[0])=='aether':
#            emMes.add_field(name='Type', value=':sun_with_face:', inline=True)
#        elif str(htmlCd.search('class="transient-container {} transient')[0])=='nether':
#            emMes.add_field(name='Type', value=':new_moon_with_face:', inline=True)
#        elif str(htmlCd.search('class="transient-container {} transient')[0])=='infernal':
#            emMes.add_field(name='Type', value=':smiling_imp:', inline=True)
#        elif str(htmlCd.search('class="transient-container {} transient')[0])=='valiant':
#            emMes.add_field(name='Type', value=':cop:', inline=True)
#        elif str(htmlCd.search('class="transient-container {} transient')[0])=='world':
#            emMes.add_field(name='Type', value=':earth_asia:', inline=True)
#        emMes.set_image(url=str(htmlCd.search('<div class="artwork"><img src=\"{}\"/></div>')[0]))
#        emMes.set_footer(text='Artist - '+str(htmlCd.search('title=\"Illustrators\">{}</a>')[0]),icon_url=str(htmlCd.search('<td class="icon"><img src="{}"')[0]))
#        emMes.set_thumbnail(url=str(htmlCd.search('<td class="icon"><img src="{}"')[0]))
#        return True, emMes
#    else:
#        return False, 'No se ha encontrada nada sobre `'+y+'` :thinking:\nPrueba buscando con otro personaje.'
