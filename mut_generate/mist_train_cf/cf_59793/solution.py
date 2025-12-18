"""
QUESTION:
Given two vessels departing from the same point and traveling at right angles to each other, write a function `calculate_distance` that calculates the distance between them after a certain amount of time. The function should take the speed of the first vessel, the speed of the second vessel, and the time traveled as inputs, and return the distance between the vessels as the hypotenuse of a right triangle, calculated using the Pythagorean theorem.
"""

import math

def calculate_distance(speed1, speed2, time):
    """
    Calculate the distance between two vessels traveling at right angles to each other.

    Args:
        speed1 (float): The speed of the first vessel.
        speed2 (float): The speed of the second vessel.
        time (float): The time traveled.

    Returns:
        float: The distance between the vessels.
    """
    # Calculate the distance traveled by each vessel
    distance1 = speed1 * time
    distance2 = speed2 * time
    
    # Use the Pythagorean theorem to calculate the distance between the vessels
    distance = math.sqrt(distance1 ** 2 + distance2 ** 2)
    
    return distance