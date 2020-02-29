import googlemaps
import pprint
import time

latlondict = {'25.252777, 55.364445'}

API_KEY = 'AIzaSyCV-wrawCG8i8cmnmVoecV4M72l1afcjXM'

gmaps = googlemaps.Client(key=API_KEY)

places_result = gmaps.places_nearby(location='55.944734, -3.187243', radius=40000, open_now=False, type='airport')

# pprint.pprint(places_result)aq1

# pause the script for 3 seconds
# time.sleep(3)

# used to get next 20 results
# places_result = gmaps.places_nearby(page_token=places_result['next_page_token'])

pprint.pprint(places_result)
