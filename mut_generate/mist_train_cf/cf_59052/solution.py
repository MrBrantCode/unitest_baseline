"""
QUESTION:
Write a function named `total_distance` to calculate the total distance covered by a vehicle in a 5-hour journey. The vehicle starts at an initial velocity and accelerates by a fixed rate every hour. The function should take two parameters: the initial velocity and the acceleration rate, both in kilometers per hour, and return the total distance covered in kilometers.
"""

def total_distance(initial_velocity, acceleration_rate):
    """
    Calculate the total distance covered by a vehicle in a 5-hour journey.

    Parameters:
    initial_velocity (float): The initial velocity of the vehicle in km/h.
    acceleration_rate (float): The acceleration rate of the vehicle in km/h.

    Returns:
    float: The total distance covered by the vehicle in km.
    """
    total_distance = 0
    velocity = initial_velocity
    for _ in range(5):
        total_distance += velocity
        velocity += acceleration_rate
    return total_distance