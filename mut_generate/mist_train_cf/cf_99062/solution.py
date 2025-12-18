"""
QUESTION:
Create a function named `distance` that calculates the distance in kilometers between two points on Earth given their latitudes and longitudes. The function should take four arguments: `lat1`, `lon1`, `lat2`, and `lon2`, representing the latitude and longitude of the first and second points, respectively. Assume the Earth is a perfect sphere with a radius of 6371 kilometers.
"""

import math

def distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance in kilometers between two points on Earth given their latitudes and longitudes.
    
    Args:
    lat1 (float): Latitude of the first point.
    lon1 (float): Longitude of the first point.
    lat2 (float): Latitude of the second point.
    lon2 (float): Longitude of the second point.
    
    Returns:
    float: Distance between the two points in kilometers.
    """
    R = 6371  # Earth radius in kilometers
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance