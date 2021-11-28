from requests import get
from random import randint

def getImages(tagsList, limit = 1):
    if not limit.isdigit():
        tagsList.append(limit)
        limit = '1'
    elif int(limit) > 50:
        raise Exception('Solo pueden buscarse hasta 50 imágenes :face_with_monocle:')

    tags = '+'.join(tagsList)
    URL = f'https://e621.net/posts.json?limit=50&tags={tags}'

    Headers = {'user-agent': 'OtarinOhtome/1.0'}
    r = get(URL, headers=Headers)
    if r.status_code != 200:
        raise Exception('Ha ocurrido un problema al buscar :pensive: probá nuevamente')

    posts = r.json()['posts']
    if posts:
        postsData = []
        for x in range(int(limit)):
            index = randint(0, 49)
            post = posts[index]
            
            data = {
                'id':post['id'],
                'url':post['file']['url'],
                'author':post['tags']['artist'][0]
            }

            postsData.append(data)
    else:
        return []

    return postsData
