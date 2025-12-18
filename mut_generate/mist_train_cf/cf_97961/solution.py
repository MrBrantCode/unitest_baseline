"""
QUESTION:
Define a function `find_intersection` that takes two lists of geographic coordinates (`coords1` and `coords2`) and a radius in kilometers as input, and returns a list of pairs of points, one from each input list, that are within the given radius of each other. The function should use the Haversine formula to calculate the great circle distance between two points on the Earth's surface.
"""

import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371 # Radius of the Earth in kilometers
    return c * r

def find_intersection(coords1, coords2, radius):
    intersection = []
    for coord1 in coords1:
        for coord2 in coords2:
            if haversine(coord1[0], coord1[1], coord2[0], coord2[1]) <= radius:
                intersection.append((coord1, coord2))
    return intersection