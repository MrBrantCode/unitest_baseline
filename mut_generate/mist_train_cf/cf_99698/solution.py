"""
QUESTION:
Write a function named `distance(lat1, lon1, lat2, lon2)` that calculates the distance between two coordinates on Earth using the Haversine formula. The function should take four arguments: the latitude and longitude of the first location (`lat1` and `lon1`), and the latitude and longitude of the second location (`lat2` and `lon2`). The function should return the distance in kilometers. Assume the Earth's radius is approximately 6371 kilometers.
"""

import math
def distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance