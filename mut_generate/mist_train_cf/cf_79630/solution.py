"""
QUESTION:
Write a function called `average_speed` that calculates the average speed for a circular tour given the total distance, the distance of the descent, the speed of the descent, and the speed of the ascent. The function should take four parameters: `total_distance`, `descent_distance`, `descent_speed`, and `ascent_speed`, and return the average speed of the entire trip.
"""

def average_speed(total_distance, descent_distance, descent_speed, ascent_speed):
    """
    Calculate the average speed for a circular tour.

    Parameters:
    total_distance (float): The total distance of the trip.
    descent_distance (float): The distance of the descent.
    descent_speed (float): The speed of the descent.
    ascent_speed (float): The speed of the ascent.

    Returns:
    float: The average speed of the entire trip.
    """
    # Calculate the time taken for the descent
    descent_time = descent_distance / descent_speed
    
    # Calculate the time spent on the ascent
    ascent_time = (total_distance - descent_distance) / ascent_speed
    
    # Calculate the total time spent
    total_time = descent_time + ascent_time
    
    # Calculate the average speed
    avg_speed = total_distance / total_time
    
    return avg_speed