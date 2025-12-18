"""
QUESTION:
Calculate the location error between the actual location of a sea turtle and the location recorded by a satellite tracking tag. The actual and recorded locations are represented by latitude and longitude coordinates. Implement a function named `calculate_location_error` that takes the actual and recorded latitude and longitude coordinates as input and returns the location error in kilometers, using the Haversine formula to calculate the distance between the two points.
"""

import math

def calculate_location_error(actual_lat, actual_lon, recorded_lat, recorded_lon):
    """
    Calculate the location error between the actual location of a sea turtle and the location recorded by a satellite tracking tag.
    
    Parameters:
    actual_lat (float): Actual latitude of the sea turtle
    actual_lon (float): Actual longitude of the sea turtle
    recorded_lat (float): Recorded latitude of the sea turtle from the tag
    recorded_lon (float): Recorded longitude of the sea turtle from the tag
    
    Returns:
    float: Location error in kilometers
    """
    R = 6371  # Earth's radius in km
    lat_diff = math.radians(recorded_lat - actual_lat)
    lon_diff = math.radians(recorded_lon - actual_lon)
    a = math.sin(lat_diff/2)**2 + math.cos(math.radians(actual_lat)) * math.cos(math.radians(recorded_lat)) * math.sin(lon_diff/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance