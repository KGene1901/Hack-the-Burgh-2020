import requests

details = {'OriDest':'LHR', 'InitDest':'HKG', 'AltDest':'DXB'}

headers = {'api-key': 'hack-the-burgh-2020',}

def scoring(score):

    pointsPerXAdmission = 2

    bonusPt = (score/6000)*pointsPerXAdmission   

    return bonusPt

def comparePoints(headers, details):
    params = (('routes', details['OriDest']+','+details['InitDest']+';'+ details['OriDest']+','+details['AltDest']),)

    response = requests.get('https://www.skyscanner.net/g/chiron/api/v1/eco/average-emissions', headers=headers, params=params)

    r =response.json()

    CO2_saved = r[1]['emissions'] - r[0]['emissions']

    print("Congratulations, you saved {} CO2 emissions".format(round(CO2_saved, 3)))

    return round(scoring(CO2_saved),0)

if __name__ == "__main__":
    bonusPt = comparePoints(headers, details)
    print(bonusPt)

        


