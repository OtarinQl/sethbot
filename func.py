from requests_html import HTMLSession

def twitter(x):
#La función toma como entrada un enlace de Twiter, lo analiza y toma el resto de imágenes contenidas en este.
    session = HTMLSession()
    r = session.get(x)
    img = r.html.find('.AdaptiveMedia-container', first=True).search_all('data-image-url=\"{}\"')
    if len(img)>1:
        y = 1
        x1 = ''
        while y < len(img):
            x1=x1+str(img[y])[10:(len(str(img[y]))-7)]+'\n'
            y = y+1
        return x1
    else:
        return 'No hay nada qué agregar :thinking:'

def housamo(y,z = '3'):
#La función toma como entrada el nombre del personaje y lo añade al enlace de la wiki de Housamo para buscar información de este.
    session = HTMLSession()
    r = session.get('https://wiki.housamo.xyz/'+y.capitalize())
    if str(r)!='<Response [404]>':
        n = 0
        htmlCd = r.html.find('#transient0',first=True)
        if z.lower() != 'variant':
            while z != str(htmlCd.search('<th>Rarity</th>\n<td>{}</td>')[0]):
                n = n+1
                htmlCd = r.html.find('#transient' + str(n), first=True)
        else:
            while htmlCd.search('<th>Variant</th>\n<td>{}</td>')==None:
                n = n+1
                htmlCd = r.html.find('#transient' + str(n), first=True)
        mens = ''
        for x in range(0,int(htmlCd.search('<th>Rarity</th>\n<td>{}</td>')[0])):
            mens = mens + ':star:'
        mens = '**Rarity** '+mens+' '
        mens = mens+'**Cost** '+str(htmlCd.search('<th>Cost</th>\n<td>{}</td>')[0])+'\n**HP** '
        mens = mens + str(htmlCd.search('<th>HP</th>\n<td>{}</td>')[0])+' **ATK** '
        mens = mens + str(htmlCd.search('<th>ATK</th>\n<td>{}</td>')[0])+'\n**Weapon** '
        if str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Slash':
            mens = mens + ':crossed_swords:'
        elif str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Blow':
            mens = mens + ':boxing_glove:'
        elif str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Shot':
            mens = mens + ':bow_and_arrow:'
        elif str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Snipe':
            mens = mens + ':gun:'
        elif str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Magic':
            mens = mens + ':sparkles:'
        elif str(htmlCd.search('alt="Weapon Spread {}.')[0])=='Thrust':
            mens = mens + ':pen_fountain:'
        mens = mens + ' **Type** '
        if str(htmlCd.search('class="transient-container {} transient')[0])=='all-round':
            mens = mens + ':regional_indicator_a: :regional_indicator_l: :regional_indicator_l:'
        elif str(htmlCd.search('class="transient-container {} transient')[0])=='wood':
            mens = mens + ':seedling:'
        elif str(htmlCd.search('class="transient-container {} transient')[0])=='fire':
            mens = mens + ':fire:'
        elif str(htmlCd.search('class="transient-container {} transient')[0])=='water':
            mens = mens + ':ocean:'
        elif str(htmlCd.search('class="transient-container {} transient')[0])=='aether':
            mens = mens + ':sun_with_face:'
        elif str(htmlCd.search('class="transient-container {} transient')[0])=='nether':
            mens = mens + ':new_moon_with_face:'
        elif str(htmlCd.search('class="transient-container {} transient')[0])=='infernal':
            mens = mens + ':smiling_imp:'
        elif str(htmlCd.search('class="transient-container {} transient')[0])=='valiant':
            mens = mens + ':cop:'
        elif str(htmlCd.search('class="transient-container {} transient')[0])=='world':
            mens = mens + ':park:'
        return True, mens, str(htmlCd.search('<div class="artwork"><img src=\"{}\"/></div>')[0]), str(htmlCd.search('<td class="icon"><img src="{}"')[0])
    else:
        return False, 'No se ha encontrada nada sobre `'+y+'`:thinking:\nPruebe buscar con otro personaje.'
