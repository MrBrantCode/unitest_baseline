"""
QUESTION:
Write a function `calculateDistance` that takes four parameters: `lat1` (latitude of point 1 in degrees), `lon1` (longitude of point 1 in degrees), `lat2` (latitude of point 2 in degrees), and `lon2` (longitude of point 2 in degrees). The function should return the distance in kilometers between the two points using the Haversine formula, assuming a mean Earth radius of 6371 kilometers.
"""

import math

def calculateDistance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return distance