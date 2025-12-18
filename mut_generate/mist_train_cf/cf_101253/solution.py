"""
QUESTION:
Create a function `distance(lat1, lon1, lat2, lon2)` to calculate the distance in kilometers between two coordinates (lat1, lon1) and (lat2, lon2) on the surface of the Earth. The function should use the Haversine formula. Assume the radius of the Earth is 6371 kilometers.
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