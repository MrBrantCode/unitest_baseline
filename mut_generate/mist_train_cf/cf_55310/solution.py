"""
QUESTION:
Write a function `calculate_mean_speed` that calculates the mean speed for a round trip between two locations. The vehicle travels from location A to location B at 40km/h and returns to location A at 60km/h. Assume the distance from A to B is "d" km.
"""

def calculate_mean_speed(d):
    """
    Calculate the mean speed for a round trip between two locations.

    Args:
        d (float): The distance from location A to location B in km.

    Returns:
        float: The mean speed in km/h.
    """
    total_distance = 2 * d
    total_time = d / 40 + d / 60
    mean_speed = total_distance / total_time
    return mean_speed