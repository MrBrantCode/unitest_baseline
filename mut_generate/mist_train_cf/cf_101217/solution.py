"""
QUESTION:
Write a function `calculate_location_error` that takes the actual latitude and longitude of a sea turtle, as well as the recorded latitude and longitude from a satellite tracking tag, and returns the location error in kilometers. Use the Haversine formula to calculate the distance between the two points on the Earth's surface, assuming a radius of 6371 kilometers.
"""

import math

def calculate_location_error(actual_lat, actual_lon, recorded_lat, recorded_lon):
    """
    Calculate the location error between the actual location of a sea turtle and the recorded location from a satellite tracking tag.
    
    Parameters:
    actual_lat (float): Actual latitude of the sea turtle.
    actual_lon (float): Actual longitude of the sea turtle.
    recorded_lat (float): Recorded latitude from the satellite tracking tag.
    recorded_lon (float): Recorded longitude from the satellite tracking tag.
    
    Returns:
    float: Location error in kilometers.
    """
    R = 6371  # Earth's radius in km
    lat_diff = math.radians(recorded_lat - actual_lat)
    lon_diff = math.radians(recorded_lon - actual_lon)
    a = math.sin(lat_diff/2)**2 + math.cos(math.radians(actual_lat)) * math.cos(math.radians(recorded_lat)) * math.sin(lon_diff/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance