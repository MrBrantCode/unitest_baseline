"""
QUESTION:
Write a function named `distance_between_two_points` to calculate the distance between two points on Earth specified by latitude and longitude in kilometers using the WGS84 system. The function should take four parameters: `lat1`, `lon1`, `lat2`, and `lon2`, which represent the coordinates of the two points in degrees.
"""

import math

def distance_between_two_points(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on Earth specified by latitude and longitude in kilometers using the WGS84 system.

    Parameters:
    lat1 (float): The latitude of the first point in degrees.
    lon1 (float): The longitude of the first point in degrees.
    lat2 (float): The latitude of the second point in degrees.
    lon2 (float): The longitude of the second point in degrees.

    Returns:
    float: The distance between the two points in kilometers.
    """

    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat_rad1 = math.radians(lat1)
    lon_rad1 = math.radians(lon1)
    lat_rad2 = math.radians(lat2)
    lon_rad2 = math.radians(lon2)

    # Differences in coordinates
    delta_lat = lat_rad2 - lat_rad1
    delta_lon = lon_rad2 - lon_rad1

    # Haversine formula
    a = math.sin(delta_lat / 2)**2 + math.cos(lat_rad1) * math.cos(lat_rad2) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate distance
    distance = R * c

    return distance