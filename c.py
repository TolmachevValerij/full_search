import sys
from io import BytesIO
import requets
from PIL import Image

from PYGAME import gts

ttf = ' '.join(sys.argv[1:])

gas = 'http://geocode-maps.yandex.ru/1.x/'

gp = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': ttf,
    'format': 'json'
}
response = requets.get(gas, params=gp)

if not response:
    pass

json_response = response.json()
toponym = json_response['response']['GetObjectCollection'][
        'featureMember'][0]['GetObject']

tc = toponym['Point']['pos']
tl, la = tc.split(' ')
d = '0.005'

mp = {
    'll': ','.join([tl, la]),
    'spn': gts(toponym),
    'l': "map",
    'pt': ','.join([tl, la] + ['pm2rdm'])
}

mas = 'http://static-maps.yandex.ru/1.x/'
response = requets.get(mas, params=mp)

Image.open(BytesIO(
    response.content)).show()
