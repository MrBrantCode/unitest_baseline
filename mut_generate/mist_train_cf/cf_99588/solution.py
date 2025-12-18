"""
QUESTION:
Implement a function `calculate_location_error` that takes the actual and recorded latitude and longitude of a location as input and returns the location error in kilometers. The location error is the distance between the actual location and the recorded location, calculated using the Haversine formula. The function should use the Earth's radius as 6371 kilometers.
"""

import math

def calculate_location_error(actual_lat, actual_lon, recorded_lat, recorded_lon):
    """
    Calculate the location error in kilometers using the Haversine formula.

    Args:
        actual_lat (float): The actual latitude of the location.
        actual_lon (float): The actual longitude of the location.
        recorded_lat (float): The recorded latitude of the location.
        recorded_lon (float): The recorded longitude of the location.

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