import requests
from requests import get 

ip = get('https://api.ipify.org').text
api = {'INSERT API KEY'}

response = requests.get('http://api.ipstack.com/'+ip+'?'+'access_key='+api)
r1 = response.json()

lati = r1['latitude']
longi = r1['longitude']

# print(lat, long)