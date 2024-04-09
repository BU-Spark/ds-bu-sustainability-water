import re 
import math



def street_distance(add1, add2):
    ''' Returns the difference in street numbers
        if the two addresses are on the same street.
        If addresses are not on the same street, will return infinity
    '''

    REGEX = r"(\d+)(.+)"
    parts1 = re.fullmatch(REGEX, add1)
    parts2 = re.fullmatch(REGEX, add2)

    assert parts1
    assert parts2


    num1 = int(parts1.group(1))
    num2 = int(parts2.group(1))

    street1 = parts1.group(2)
    street2 = parts2.group(2)


    street1 = convert_street_to_full(street1)
    street2 = convert_street_to_full(street2)


    if street1.lower() != street2.lower():
        return math.inf

    return abs(num1 - num2)


ABREVIATIONS = {
    'st': 'street',
    'rd': 'road',
    'ave': 'avenue'
}

def convert_street_to_full(street):
    words = street.split(' ')
    suffix = words[-1]
    if suffix.lower() in ABREVIATIONS.keys():
        replacement = ABREVIATIONS[suffix.lower()]
        new_street = " ".join(words[:-1]) + " " + replacement
        return new_street
    else:
        return street


def test_convert_street_to_full():

    i1 = '928 COMMONWEALTH AVENUE, Boston, MA'
    i2 = '285 Babcock St'
    a2 = '285 Babcock street'
    assert convert_street_to_full(i1) == i1
    assert convert_street_to_full(i2) == a2


def test_street_distance():
    assert street_distance('928 Commonwealth ave, Boston, MA', '940 Commonwealth ave, Boston, MA') == 12
    assert street_distance('50 Buswell street, Boston, MA', '940 Commonwealth ave, Boston, MA') == math.inf