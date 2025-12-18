"""
QUESTION:
Write a function named `calculate_distance` to calculate the cumulative distance traveled over a given period of time. The vehicle's initial speed and the hourly speed increment are provided. The function should take two parameters: `initial_speed` (in km/h) and `hours`, and return the cumulative distance traveled.
"""

def calculate_distance(initial_speed, hours):
    """
    Calculate the cumulative distance traveled over a given period of time.
    
    Parameters:
    initial_speed (int): The vehicle's initial speed in km/h.
    hours (int): The number of hours.
    
    Returns:
    int: The cumulative distance traveled.
    """
    cumulative_distance = 0
    speed = initial_speed
    
    for _ in range(hours):
        cumulative_distance += speed
        speed += 20  # Assuming a constant hourly speed increment of 20 km/h
    
    return cumulative_distance