"""
QUESTION:
Write a function `calculate_travel_time` to compute the time it takes to travel a certain distance at a constant speed. The function should take two parameters: `distance` and `speed`, both in kilometers. The function should return the time in hours.
"""

def calculate_travel_time(distance, speed):
    """
    Calculate the time it takes to travel a certain distance at a constant speed.

    Parameters:
    distance (float): The distance to be traveled in kilometers.
    speed (float): The constant speed in kilometers per hour.

    Returns:
    float: The time it takes to travel the distance in hours.
    """
    return distance / speed