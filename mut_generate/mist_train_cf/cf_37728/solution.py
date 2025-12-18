"""
QUESTION:
Create a Python function `calculate_distance` that takes four parameters: `lat1`, `lon1`, `lat2`, and `lon2`, representing the latitude and longitude of two points on the Earth's surface. The function should return the distance between the two points in kilometers, calculated using the Haversine formula, which assumes a spherical Earth with a radius of approximately 6371 kilometers. The input parameters `lat1`, `lon1`, `lat2`, and `lon2` are in decimal degrees.
"""

import math

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance