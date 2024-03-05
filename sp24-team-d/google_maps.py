import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GOOGLE_MAPS_API = os.getenv('GOOGLE_MAPS')

def get_distance(origin, destination):
    MODE = 'walking'

    url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    params = {
        'key': GOOGLE_MAPS_API,
        'origins': origin,
        'destinations': destination,
        'mode': MODE
    }

    res = requests.get(url, params=params)

    if res.status_code == 200:
        body = res.json()
        row = body['rows'][0]
        element = row['elements'][0]
        distance = element['duration']['value']
        return distance
    else:
        raise Exception(f"Error: {res.status_code}")

def get_distance_matrix_large(origins, destinations, file):
    results = []
    with open(file, 'a') as f:
        for origin in origins:
            for destination in destinations:
                results = get_distance(origin, destination)
                json.dump(results, f)


    return results


def get_distance_matrix(origins, destinations):
    ''' Given a list of addresses, compute a distance matrix that has all walking times
        Calls Google Maps API
    '''

    DELIMITER = "|"
    MODE = 'walking'

    origin_str = DELIMITER.join(origins)
    destination_str = DELIMITER.join(destinations)

    url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    params = {
        'key': GOOGLE_MAPS_API,
        'origins': origin_str,
        'destinations': destination_str,
        'mode': MODE
    }

    res = requests.get(url, params=params)

    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"Error: {res.status_code}")


if __name__ == '__main__':
    distance = get_distance('91 Bay State Rd, Boston, MA', '52 Buswell Street, Boston, MA')
    print(distance)
    
