import requests
from bs4 import BeautifulSoup

def search(tags, imageQuantity = 3):
    tags = tags.replace(' ', '%20')
    r = requests.get("https://e621.net/post/index/1/" + tags, headers= {'User-Agent' : 'PostmanRuntime/7.15.0'})
    soup = BeautifulSoup(r.text, "html.parser")
    thumbnails = soup.find_all(class_="thumb")
    links = []
    for x in range(min(imageQuantity, len(thumbnails))):
        link = thumbnails[x].a
        links.append(link.get('href'))
    
    images = []
    for link in links:
        r = requests.get('https://e621.net' + link, headers= {'User-Agent' : 'PostmanRuntime/7.15.0'})
        soup = BeautifulSoup(r.text, "html.parser")
        image = soup.find(id='image')
        if image is not None:
            images.append(image.get('src'))

    return images
