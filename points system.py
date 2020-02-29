import requests
import random

details = {'OriDest':'LHR', 'InitDest':'HKG', 'AltDest':'DXB'} # sample location

CF = [{'item':'beef', 'amt':36.4}, {'item':'cheese', 'amt':13.5}, {'item':'chicken', 'amt':6.9}, {'item':'black coffee', 'amt':0.021}, {'item':'dairy milk', 'amt':1.4}, {'item':'wood', 'amt':0.4}]

headers = {'api-key': 'hack-the-burgh-2020',}


def compareCF(CO2_saved):

    n = random.randint(0,5)
    item = CF[n]['item']
    amt = CF[n]['amt']

    num = round(CO2_saved/amt, 2)

    if item == 'wood':
        print('Thats about {} woods burned!'.format(num))
    else:
        print('Thats about {} {} consumed!'.format(num,item))


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
    compareCF(CO2_saved)

    return round(scoring(CO2_saved),0)

if __name__ == "__main__":
    bonusPt = compareCO2(headers, details)
    print('Bonus point earned:', bonusPt)

        


