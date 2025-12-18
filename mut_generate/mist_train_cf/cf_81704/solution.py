"""
QUESTION:
Write a function `calculate_distance_difference` that takes the speeds of two vehicles in km/h and the time they travel in hours as input and returns the distance difference between them, assuming they travel in opposite directions from the same starting point.
"""

def calculate_distance_difference(speed1, speed2, time):
    """
    Calculate the distance difference between two vehicles moving in opposite directions.

    Args:
    speed1 (float): The speed of the first vehicle in km/h.
    speed2 (float): The speed of the second vehicle in km/h.
    time (float): The time they travel in hours.

    Returns:
    float: The distance difference between the two vehicles.
    """
    return (speed1 + speed2) * time