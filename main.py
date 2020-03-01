import sys
from map_stuff.google_api_attraction import getLatLngattr
from map_stuff.google_api_airport import getLatLng
from points_system import *

current_lat = str(25.197525)
current_lng = str(55.274288)
loca = current_lat + ', ' + current_lng

# Gets original location (location's lat and lng come from gene user_location.
ori_loca = getLatLng(loca)

init_lat = str(51.470020)
init_lng = str(-0.454295)
init = init_lat + ', ' + init_lng

# gets initial destination airport according to user input
init_dest = getLatLng(init)

# gets the location of attraction and find closest similar attraction
attract = getLatLngattr(current_lat, current_lng, 'beach')
alt_loca = str(attract[0]) + ', ' + str(attract[1])

Alt_dest = getLatLng(alt_loca)

# creates dictionary
details = {'OriDest': ori_loca, 'InitDest': init_dest, 'AltDest': Alt_dest}
print(details)

# initiate point system
if __name__ == "__main__":
    bonusPt = compareCO2(headers, details)
    print('Bonus point earned:', bonusPt)
