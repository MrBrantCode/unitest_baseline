"""
QUESTION:
Write a function named `distance` that calculates the distance between two coordinates on the Earth's surface using the Haversine formula. The function should take four arguments: `lat1`, `lon1`, `lat2`, and `lon2`, which represent the latitude and longitude of the two coordinates in decimal degrees. The function should return the distance in kilometers.
"""

import math
def distance(lat1, lon1, lat2, lon2):
    R = 6371 # Earth radius in kilometers
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance