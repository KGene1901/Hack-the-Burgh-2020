import sys
from map_stuff.google_api_attraction import getLatLngattr
from map_stuff.google_api_airport import getLatLng
from points_system import *
from user_location import *
import os
import platform

def clear():

	if (os.name == "nt"): 
		os.system("cls")
	   
	else:
	   os.system("clear")

# current_lat = str(25.197525)
# current_lng = str(55.274288)

current_lat = str(lati)
current_lng = str(longi)
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
# attract = getLatLngattr(32,34, 'beach')
alt_loca = str(attract[0]) + ', ' + str(attract[1])
name = str(attract[2])
rating = str(attract[3])

Alt_dest = getLatLng(alt_loca)

# creates dictionary
details = {'OriDest': ori_loca, 'InitDest': init_dest, 'AltDest': Alt_dest}

# initiate point system
if __name__ == "__main__":
   
#-----------------------------------------------------------------------
#Main Program
#-----------------------------------------------------------------------
    clear()

    program_info = "Flight Checker\nHack the Burgh 2020\n"

    user_command = "nothing"

    print("Origin Airport:", ori_loca)
    print("Chosen Destination Airport:", init_dest)

    print("Instead of travelling to {}, to reduce your overall carbon footprints via travel, how about taking a trip to {}?".format(init_dest, Alt_dest))    
    print("There is a beach named {} that has a rating of {}".format(name,rating))
    print("Pick 1 for yes and 2 for no:")

    userInput = int(input('Enter choice:'))

    if userInput==1:
        bonusPt = compareCO2(headers, details)
        print('Bonus point earned:', bonusPt)
    else:
        # print("Ok, if you say so ")
        print('Your flight to {} has been booked'.format(init_dest))
        

    

