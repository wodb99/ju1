import json

a = dict()
a['name'] = 'sanghi'
a['price'] = 4900
a['brand'] = 'mcdonald'

# Encoding 메서드 json.dumps()
b = json.dumps(a, indent=2)
print(b)

# Decoding 메서드 json.loads()
c = json.loads(b)
print(c)

import requests
import json

url = 'https://pokeapi.co/docs/v2'
r = requests.get(url).text  # .json은 딕셔너리로, .text하면 json으로
print(r)