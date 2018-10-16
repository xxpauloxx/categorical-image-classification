import flickrapi
import requests
import shutil
import sys
import os

from PIL import Image
from resizeimage import resizeimage

DATA_PATH = 'data'
DESTINATION_PATH = 'data/train/{}/{}.jpg'

API_KEY = os.environ.get('FLICKR_API_KEY')
SECRET = os.environ.get('FLICKR_SECRET')


def mkdir_if_not_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)


def resize_image(path):
    with Image.open(path) as image:
        cover = resizeimage.resize_cover(image, [128, 128])
        cover.save(DESTINATION_PATH.format(keyword, i), image.format)


flickr = flickrapi.FlickrAPI(API_KEY, SECRET, cache=True)
keyword = sys.argv[1]

mkdir_if_not_exists(DATA_PATH)
mkdir_if_not_exists('{}/train'.format(DATA_PATH))
mkdir_if_not_exists('{}/train/{}'.format(DATA_PATH, keyword))

photos = flickr.walk(
    text=keyword, tag_mode='all', tags=keyword, extras='url_c',
    per_page=100, sort='relevance')

urls = []
for i, photo in enumerate(photos):
    image_url = photo.get('url_c')

    if image_url is not None:
        print('Baixando imagem de {}.'.format(image_url))
        response = requests.get(image_url, stream=True)

        if response.status_code == 200:
            image_file = response.raw

            with open(DESTINATION_PATH.format(keyword, i), 'wb') as f:
                shutil.copyfileobj(image_file, f)

            resize_image(DESTINATION_PATH.format(keyword, i))

        print('Imagem foi salva!')

