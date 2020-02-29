import googlemaps
import pprint
import time

API_KEY = 'AIzaSyCV-wrawCG8i8cmnmVoecV4M72l1afcjXM'

gmaps = googlemaps.Client(key=API_KEY)

places_result = gmaps.places_nearby(location='55.944734, -3.187243', radius=40000, open_now=False, type='airport')

pprint.pprint(places_result)
