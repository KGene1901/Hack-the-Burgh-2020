import googlemaps
import pprint
import json
import time
from range_key_dict import RangeKeyDict


def getLatLng(loca):
    # latlondict = RangeKeyDict({(24, 25.25): (54, 55.36): 'DXB', (50, 51.470020): (-0.454295, 0): 'LHR', (39, 40.072498): (115, 116.597504):'PEK',(34, 35.553333): (138, 139.781113): 'HND', (32, 33.942791): (-118.410042, -117): 'LAX'})
    latlondict = RangeKeyDict({(24, 26): 'DXB', (50, 52): 'LHR', (39, 41): 'PEK', (34, 36): 'HND', (32, 34): 'LAX', (54, 56): 'EDI'})

    API_KEY = 'AIzaSyCV-wrawCG8i8cmnmVoecV4M72l1afcjXM'

    gmaps = googlemaps.Client(key=API_KEY)

    # radius in meters

    places_result = gmaps.places_nearby(location=loca, radius=40000, open_now=False, type='airport')

    # pause the script for 3 seconds
    # time.sleep(3)

    # used to get next 20 results
    # places_result = gmaps.places_nearby(page_token=places_result['next_page_token'])

    # pprint.pprint(places_result)

    # loop through each place in the results
    for place in places_result['results']:
        # define my latlong
        my_place_id = place['place_id']
        my_fields = ['geometry/location/lat', 'geometry/location/lng']
        place_details = gmaps.place(place_id=my_place_id, fields=my_fields)
        # print(place_details)
        lat = round(place_details['result']['geometry']['location']['lat'], 2)
        long = str(round(place_details['result']['geometry']['location']['lng'], 2))
        # cords = lat + ', ' + long
        # print(cords)
        # print(place_details['result']['geometry']['location']['lat'])

        #print(latlondict[lat])

        if latlondict[lat] == latlondict[lat]:

            return latlondict[lat]


#getLatLng()
