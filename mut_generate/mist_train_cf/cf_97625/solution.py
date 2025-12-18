"""
QUESTION:
Write a function called `calculate_location_error` that calculates the location error in kilometers between the actual location of a sea turtle and the location recorded by a satellite tracking tag. The function should take as input the actual latitude and longitude and the recorded latitude and longitude. The location error should be calculated using the Haversine formula, assuming the Earth's radius is 6371 kilometers.
"""

import math

def calculate_location_error(actual_lat, actual_lon, recorded_lat, recorded_lon):
    """
    Calculate the location error in kilometers between the actual location of a sea turtle and the location recorded by a satellite tracking tag.
    
    Parameters:
    actual_lat (float): The actual latitude of the sea turtle.
    actual_lon (float): The actual longitude of the sea turtle.
    recorded_lat (float): The recorded latitude of the sea turtle from the satellite tracking tag.
    recorded_lon (float): The recorded longitude of the sea turtle from the satellite tracking tag.
    
    Returns:
    float: The location error in kilometers.
    """
    R = 6371  # Earth's radius in km
    lat_diff = math.radians(recorded_lat - actual_lat)
    lon_diff = math.radians(recorded_lon - actual_lon)
    a = math.sin(lat_diff/2)**2 + math.cos(math.radians(actual_lat)) * math.cos(math.radians(recorded_lat)) * math.sin(lon_diff/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c