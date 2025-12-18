"""
QUESTION:
Write a function named "calculate_mean_speed" that takes two velocities as input, representing the speed of a vehicle going from location A to location B and back to location A. The function should return the mean speed for the round trip.
"""

def calculate_mean_speed(speed1, speed2):
    """
    Calculate the mean speed for a round trip.

    The mean speed is 2 times the product of the two velocities divided by the sum of the two velocities.

    Args:
        speed1 (float): The speed of the vehicle from location A to location B.
        speed2 (float): The speed of the vehicle from location B back to location A.

    Returns:
        float: The mean speed for the round trip.
    """
    return 2 * speed1 * speed2 / (speed1 + speed2)