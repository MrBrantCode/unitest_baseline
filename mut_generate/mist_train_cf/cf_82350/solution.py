"""
QUESTION:
Given two cyclists starting from the same point on a circular track with the slower cyclist cycling at 'S' km/h, find the expression relating the circumference and speed with respect to time 'T' to determine the distance between them after 'T' hours, considering the faster cyclist's speed is 20% faster than the slower cyclist's.
"""

def calculate_distance(S, T):
    """
    Calculate the distance between two cyclists after a certain time.

    The slower cyclist's speed is S km/h, and the faster cyclist's speed is 20% faster.
    The time is given in hours.

    Args:
        S (float): The speed of the slower cyclist in km/h.
        T (float): The time in hours.

    Returns:
        float: The distance between the two cyclists.
    """
    # Calculate the speed of the faster cyclist
    faster_speed = 1.2 * S
    
    # Calculate the difference in speed
    speed_difference = faster_speed - S
    
    # Calculate the distance
    distance = speed_difference * T
    
    return distance