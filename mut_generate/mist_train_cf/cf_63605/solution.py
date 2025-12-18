"""
QUESTION:
Create a function called `calculate_next_position` that takes in the moment of inertia, angular momentum, and time, and returns the next position of a spinning dice in a 3D space, considering the correct relationship between angular momentum and angular velocity. The function should correctly calculate the angular velocity from the angular momentum and the moment of inertia, and use this to determine the next position.
"""

def calculate_next_position(moment_of_inertia, angular_momentum, time, current_position):
    """
    Calculate the next position of a spinning dice in a 3D space.

    Args:
    moment_of_inertia (float): The moment of inertia of the dice.
    angular_momentum (float): The angular momentum of the dice.
    time (float): The time step.
    current_position (float): The current position of the dice.

    Returns:
    float: The next position of the dice.
    """
    angular_velocity = angular_momentum / moment_of_inertia  # Correct manipulation
    next_position = current_position + angular_velocity * time
    return next_position