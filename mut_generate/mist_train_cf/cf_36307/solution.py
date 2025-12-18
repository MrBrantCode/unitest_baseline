"""
QUESTION:
Implement the `calculateDistance` function that calculates the distance between two points on the Earth's surface given their geographical coordinates. The function should take four parameters: `lat1`, `long1`, `lat2`, and `long2`, representing the latitudes and longitudes of the two points in degrees. The function should return the distance between the two points in kilometers, rounded to two decimal places. Use the Earth's mean radius as 6,371 kilometers.
"""

import math

def calculateDistance(lat1, long1, lat2, long2):
    R = 6371  # Radius of the Earth in kilometers
    lat1_rad = math.radians(lat1)
    long1_rad = math.radians(long1)
    lat2_rad = math.radians(lat2)
    long2_rad = math.radians(long2)

    delta_lat = lat2_rad - lat1_rad
    delta_long = long2_rad - long1_rad

    a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_long/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return round(distance, 2)