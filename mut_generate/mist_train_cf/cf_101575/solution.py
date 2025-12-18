"""
QUESTION:
Write a function `calculate_location_error` that calculates the distance between the actual location of a tagged sea turtle and the location recorded by the satellite tracking tag using the Haversine formula, given the actual latitude and longitude and the recorded latitude and longitude of the turtle. The function should take four parameters: `actual_lat`, `actual_lon`, `recorded_lat`, and `recorded_lon`, and return the location error in kilometers.
"""

import math

def calculate_location_error(actual_lat, actual_lon, recorded_lat, recorded_lon):
    """
    Calculate the distance between the actual location of a tagged sea turtle and 
    the location recorded by the satellite tracking tag using the Haversine formula.

    Parameters:
    actual_lat (float): The actual latitude of the turtle.
    actual_lon (float): The actual longitude of the turtle.
    recorded_lat (float): The recorded latitude of the turtle from the tag.
    recorded_lon (float): The recorded longitude of the turtle from the tag.

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