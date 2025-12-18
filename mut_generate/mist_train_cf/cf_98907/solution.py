"""
QUESTION:
Write a function named `calculate_location_error` that calculates the distance between two geographic coordinates (latitude and longitude) using the Haversine formula, representing the location error of a satellite tracking tag on a sea turtle. The function should take four arguments: `actual_lat`, `actual_lon`, `recorded_lat`, and `recorded_lon`, representing the actual location of the turtle and the location recorded by the tag, respectively. The function should return the location error in kilometers.
"""

import math

def calculate_location_error(actual_lat, actual_lon, recorded_lat, recorded_lon):
    """
    Calculate the distance between two geographic coordinates using the Haversine formula.

    Args:
    actual_lat (float): The actual latitude of the turtle.
    actual_lon (float): The actual longitude of the turtle.
    recorded_lat (float): The recorded latitude by the satellite tracking tag.
    recorded_lon (float): The recorded longitude by the satellite tracking tag.

    Returns:
    float: The location error in kilometers.
    """
    R = 6371  # Earth's radius in km
    lat_diff = math.radians(recorded_lat - actual_lat)
    lon_diff = math.radians(recorded_lon - actual_lon)
    a = math.sin(lat_diff/2)**2 + math.cos(math.radians(actual_lat)) * math.cos(math.radians(recorded_lat)) * math.sin(lon_diff/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance