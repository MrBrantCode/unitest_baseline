"""
QUESTION:
Write a function named `calculate_time` that calculates the time duration it would take for an object to attain a certain velocity, given the acceleration due to gravity. The function should take the final velocity in km/h as input, and return the time in seconds. The acceleration due to gravity is 9.8 m/s^2 and the initial velocity is 0 m/s.
"""

def calculate_time(final_velocity_kmh):
    """
    Calculate the time it takes for an object to attain a certain velocity.

    Parameters:
    final_velocity_kmh (float): The final velocity in km/h.

    Returns:
    float: The time in seconds.
    """
    # Convert velocity from km/h to m/s
    final_velocity_ms = final_velocity_kmh / 3.6
    
    # Acceleration due to gravity in m/s^2
    acceleration = 9.8
    
    # Initial velocity in m/s
    initial_velocity = 0
    
    # Calculate time
    time = (final_velocity_ms - initial_velocity) / acceleration
    
    return time