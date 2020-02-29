import requests

Origin = 'EDI'
Destination = 'DUB'

headers = {
    'api-key': 'hack-the-burgh-2020',
}

params = (
    ('routes', 'EDI,MAS'),
)

response = requests.get('https://www.skyscanner.net/g/chiron/api/v1/eco/average-emissions', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.skyscanner.net/g/chiron/api/v1/eco/average-emissions?routes=EDI,DUB', headers=headers)
r = response.json()
print(r[0]['emissions'])

