import googlemaps
import pprint
import json
import time

latlondict = {'25.25, 55.36': {'DXB'}, '51.470020, -0.454295': {'LHR'}, '40.072498, 116.597504': {'PEK'}, '35.553333, 139.781113': {'HND'}, '33.942791, -118.410042': {'LAX'}}

API_KEY = 'AIzaSyCV-wrawCG8i8cmnmVoecV4M72l1afcjXM'

gmaps = googlemaps.Client(key=API_KEY)

places_result = gmaps.places_nearby(location='25.197525, 55.274288', radius=40000, open_now=False, type='airport')

# pause the script for 3 seconds
# time.sleep(3)

# used to get next 20 results
# places_result = gmaps.places_nearby(page_token=places_result['next_page_token'])

#pprint.pprint(places_result)

# loop through each place in the results
for place in places_result['results']:
    # define my latlong
    my_place_id = place['place_id']
    my_fields = ['geometry/location/lat', 'geometry/location/lng']
    place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
    #print(place_details)
    lat = str(round(place_details['result']['geometry']['location']['lat'], 2))
    long = str(round(place_details['result']['geometry']['location']['lng'], 2))
    cords = lat + ', ' + long
    print(cords)
    #print(place_details['result']['geometry']['location']['lat'])

    if cords in latlondict.keys():
        print(cords)
