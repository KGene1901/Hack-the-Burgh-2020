import requests
from requests import get 

ip = get('https://api.ipify.org').text
api = 'b36bc7b6ea95492c25c6cb693a0e9665'

response = requests.get('http://api.ipstack.com/'+ip+'?'+'access_key='+api)
r1 = response.json()

lat = r1['latitude']
long = r1['longitude']

# print(lat, long)