
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GEOAPIFY = os.getenv('GEOAPIFY')

def get_long_lat(address):
    url = 'https://api.geoapify.com/v1/geocode/search'

    params = {
        'apiKey': GEOAPIFY,
        'text': address,
    }

    res = requests.get(url, params=params)

    if res.status_code == 200:
        features = res.json()['features'][0]
        properties = features['properties']
        lon = properties['lon']
        lat = properties['lat']
        return lat, lon
    else:
        raise Exception(f"Error: {res.status_code}")



if __name__ == '__main__':
    lat, lon = get_long_lat('96 Bay state Rd, Boston, MA, 02215')
    print(lat, lon)
    
