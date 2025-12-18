"""
QUESTION:
Write a function named `distance` that calculates the distance in kilometers between two coordinates on Earth given their latitude and longitude. The function should take four arguments: `lat1`, `lon1`, `lat2`, and `lon2`, representing the latitude and longitude of the first and second coordinates, respectively. Use the Haversine formula to calculate the distance. Assume the Earth's radius is approximately 6371 kilometers.
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