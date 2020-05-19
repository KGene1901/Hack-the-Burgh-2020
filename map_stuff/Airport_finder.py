import requests


def airport_code():
    url = "https://cometari-airportsfinder-v1.p.rapidapi.com/api/airports/by-radius"

    # radius in km
    querystring = {"radius": "100", "lng": "-155.895277", "lat": "21.265600"}

    headers = {
        'x-rapidapi-host': "cometari-airportsfinder-v1.p.rapidapi.com",
        'x-rapidapi-key': {'INSERT API KEY'}
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    location = response.json()
    print(location)
    print(location[0]['code'])


airport_code()
