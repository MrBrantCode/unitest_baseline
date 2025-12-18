"""
QUESTION:
Write a function `calculate_time_to_max_height` that calculates the time it takes for an object to reach its maximum height when projected upwards with a given initial velocity. The function should take two parameters: `initial_velocity` (in meters per second) and `gravity` (in meters per second squared), defaulting to 9.8 if not provided.
"""

def calculate_time_to_max_height(initial_velocity, gravity=9.8):
    """
    Calculate the time it takes for an object to reach its maximum height.

    Parameters:
    initial_velocity (float): Initial velocity of the object in meters per second.
    gravity (float): Acceleration due to gravity in meters per second squared. Defaults to 9.8.

    Returns:
    float: Time to reach maximum height in seconds.
    """
    return initial_velocity / gravity