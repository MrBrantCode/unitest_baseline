"""
QUESTION:
Write a function `calculate_freefall_time` that calculates the time it takes for an object to reach a certain velocity in a freefall. The function should take the target velocity in km/h as input and return the time in seconds. Assume an acceleration due to gravity of 9.8 m/s^2 and neglect air resistance.
"""

def calculate_freefall_time(target_velocity):
    """
    Calculate the time it takes for an object to reach a certain velocity in a freefall.

    Args:
    target_velocity (float): The target velocity in km/h.

    Returns:
    float: The time in seconds.
    """
    # Convert target velocity from km/h to m/s
    target_velocity_ms = target_velocity * (1000 / 3600)
    
    # Calculate time using the formula t = v / a
    acceleration_due_to_gravity = 9.8  # m/s^2
    time = target_velocity_ms / acceleration_due_to_gravity
    
    return time