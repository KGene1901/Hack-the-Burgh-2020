import requests
import random

details = {'OriDest':'LHR', 'InitDest':'HKG', 'AltDest':'DXB'} # sample location

CF = [{'item':'Beef', 'amt':36.4}, {'item':'Cheese', 'amt':13.5}, {'item':'Chicken', 'amt':6.9}, {'item':'Black Coffee', 'amt':0.021}, {'item':'Dairy Milk', 'amt':1.4}]

headers = {'api-key': 'hack-the-burgh-2020',}


def compareCF():

    n = random.randint(0,5)
    item = CF[n]['item']
    amt = CF[n]['amt']

    print(item, amt)


def scoring(score):

    pointsPerXAdmission = 2

    bonusPt = (score/6000)*pointsPerXAdmission   

    return bonusPt

def compareCO2(headers, details):
    params = (('routes', details['OriDest']+','+details['InitDest']+';'+ details['OriDest']+','+details['AltDest']),)

    response = requests.get('https://www.skyscanner.net/g/chiron/api/v1/eco/average-emissions', headers=headers, params=params)

    r =response.json()

    CO2_saved = r[1]['emissions'] - r[0]['emissions']

    print("Congratulations, you saved {} kg of CO2 emissions".format(round(CO2_saved, 3)))

    return round(scoring(CO2_saved),0)

if __name__ == "__main__":
    bonusPt = compareCO2(headers, details)
    print(bonusPt)

        


