"""
QUESTION:
Create a function `distance(lat1, lon1, lat2, lon2)` to calculate the distance between two coordinates in kilometers using the Haversine formula. The function should take four parameters: the latitude and longitude of the first coordinate, and the latitude and longitude of the second coordinate. The radius of the earth in kilometers is 6371. The function should return the distance between the two coordinates.
"""

import math
def distance(lat1, lon1, lat2, lon2):
    R = 6371  # radius of the earth in kilometers
    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance