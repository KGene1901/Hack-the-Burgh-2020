import requests

headers = {
    'api-key': 'hack-the-burgh-2020',
}

######################################################################

params = (
    ('routes', 'LHR,HKG'),
)


response = requests.get('https://www.skyscanner.net/g/chiron/api/v1/eco/average-emissions', headers=headers, params=params)

r = response.json()
print(r[0]['emissions'])

#############################################################################

