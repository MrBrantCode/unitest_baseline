"""
QUESTION:
Create a function `calculateDistance` that takes four parameters: `lat1`, `lng1`, `lat2`, and `lng2`, representing the latitude and longitude of two points in decimal degrees. The function should return the distance between the two points in kilometers, rounded to two decimal places, using the Haversine formula and the mean radius of the Earth (6,371km). The function should handle the conversion of latitude and longitude from degrees to radians internally.
"""

import math

def calculateDistance(lat1, lng1, lat2, lng2):
    R = 6371  # Radius of the Earth in kilometers
    lat1_rad = math.radians(lat1)
    lng1_rad = math.radians(lng1)
    lat2_rad = math.radians(lat2)
    lng2_rad = math.radians(lng2)

    delta_lat = lat2_rad - lat1_rad
    delta_lng = lng2_rad - lng1_rad

    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lng / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return round(distance, 2)