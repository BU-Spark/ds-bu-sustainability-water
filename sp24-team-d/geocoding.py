import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GEOCODING = os.getenv('GEOCODING')

def get_long_lat(address):

    url = 'https://geocode.maps.co/search'

    params = {
        'api_key': GEOCODING,
        'q': address,
    }

    res = requests.get(url, params=params)
    print(res)

    if res.status_code == 200:
        with open('data/temp-res.json', 'w') as f:
            json.dump(res.json(), f)
    else:
        raise Exception(f"Error: {res.status_code}")



if __name__ == '__main__':
    get_long_lat('96 Baystate Rd, Boston, MA, 02215')