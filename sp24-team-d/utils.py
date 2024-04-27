import math 

def haversine(p1, p2):
    ''' Returns haversine distance between two longitude and latitude points
            Code taken from https://www.geeksforgeeks.org/haversine-formula-to-find-distance-between-two-points-on-a-sphere
            I believe this is in kilometers
    '''
    lat1, lon1 = p1
    lat2, lon2 = p2

    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
 
    # apply formula
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c

def address_to_lat_long(address):
    ''' Returns lat, long of a given address
        Input:
            adress: string
    '''
    nominatim = Nominatim(user_agent="Geopy Library")
    loc = nominatim.geocode(address)
    print(loc.latitude, loc.longitude)
    return loc.latitude, loc.longitude

def test_address_to_lat_long():
    address_to_lat_long(r"8 St. Mary's St")
    assert False
