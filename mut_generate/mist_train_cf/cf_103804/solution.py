"""
QUESTION:
Calculate the total distance traveled by an object given its initial velocity, acceleration, and time interval, with the time interval rounded to the nearest hundredth decimal place. Create a function `calculate_distance` that takes three parameters: `initial_velocity`, `acceleration`, and `time_interval`.
"""

def calculate_distance(initial_velocity, acceleration, time_interval):
    """
    Calculate the total distance traveled by an object given its initial velocity, 
    acceleration, and time interval.

    Args:
        initial_velocity (float): The initial velocity of the object.
        acceleration (float): The acceleration of the object.
        time_interval (float): The time interval.

    Returns:
        float: The total distance traveled.
    """
    # Calculate the distance using the equation: 
    # distance = initial velocity * time + (1/2) * acceleration * time^2
    distance = initial_velocity * round(time_interval, 2) + (1/2) * acceleration * (round(time_interval, 2))**2
    return round(distance, 2)