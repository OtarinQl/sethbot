import re
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

def housamo(y):
#La función toma como entrada el nombre del personaje y lo añade al enlace de la wiki de Housamo para buscar información de este.
    session = HTMLSession()
    r = session.get('https://wiki.housamo.xyz/'+y[1].capitalize())
    if(str(r)!='<Response [404]>'):
        if(len(y)==2 or y[2]=='3'):
            htmlCd = r.html.find('#transient0',first=True)
            x = 0
        else:
            tabla = r.html.find('.toc',first=True)
            tb = re.findall('☆\d|Variant',tabla.text)
            x = 0
            while('☆'+y[2]!=tb[x]):
                x = x+1
            htmlCd = r.html.find('#transient'+str(x),first=True)
        urls = r.html.search_all('<img src=\"{}\"')
        if not re.match('.+\.png.+',str(urls[0])):
            urls = r.html.search_all('<img alt=\"{}\" src=\"{}\"')
        icon = []
        icon.append(re.findall('https://.+\.png',str(urls[x*2]))[0])
        icon.append(re.findall('https://.+\.png',str(urls[(x*2)+1]))[0])
        match = re.findall('setTimeout.+',str(htmlCd.text))
        if(len(match)>0):
            info = htmlCd.text.replace(match[0],'')
        else:
            info = htmlCd.text
        return [[y[1].capitalize(), info, icon],True]
    else:
        return ['No existe nada sobre `'+y[1]+'` :thinking:\nPrueba mandando el mensaje otra vez', False]