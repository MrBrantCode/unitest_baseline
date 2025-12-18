"""
QUESTION:
Write a function `distance(lat1, lon1, lat2, lon2)` that calculates the distance in kilometers between two points on the Earth's surface given their latitude and longitude coordinates using the Haversine formula. The Earth's radius is approximately 6371 kilometers.
"""

import math
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371 # Earth radius in kilometers
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance