"""
QUESTION:
Compute the duration in hours required to cover a given distance at a constant speed of 60 km per 45 minutes. Function name: compute_duration. The function should take the distance in kilometers as input and return the duration in hours.
"""

def compute_duration(distance_km):
    """
    Compute the duration in hours required to cover a given distance at a constant speed of 60 km per 45 minutes.

    Args:
        distance_km (float): The distance in kilometers.

    Returns:
        float: The duration in hours.
    """
    speed_kmh = 60 / 0.75  # calculate speed in km/h
    return distance_km / speed_kmh