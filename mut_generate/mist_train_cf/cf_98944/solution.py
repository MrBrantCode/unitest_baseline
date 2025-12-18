"""
QUESTION:
Create a function named `distance` that calculates the distance in kilometers between two coordinates on Earth, given their latitude and longitude in degrees. The Earth's radius is approximately 6371 kilometers.
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