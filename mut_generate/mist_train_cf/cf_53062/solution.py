"""
QUESTION:
Create a function `calculate_average_speed` that takes the speed downstream, speed upstream, and total distance as parameters. The function should calculate and return the average speed for a round trip where the total distance is evenly split between downstream and upstream. The speed should be calculated by dividing the total distance by the total time spent, where time is calculated as distance divided by speed.
"""

def calculate_average_speed(speed_downstream, speed_upstream, total_distance):
    """
    Calculate the average speed for a round trip.

    Parameters:
    speed_downstream (float): The speed downstream.
    speed_upstream (float): The speed upstream.
    total_distance (float): The total distance.

    Returns:
    float: The average speed.
    """
    # Calculate the distance for each leg of the trip, assuming it's evenly split
    distance_per_leg = total_distance / 2

    # Calculate the time spent downstream
    time_downstream = distance_per_leg / speed_downstream

    # Calculate the time spent upstream
    time_upstream = distance_per_leg / speed_upstream

    # Calculate the total time
    total_time = time_downstream + time_upstream

    # Calculate and return the average speed
    return total_distance / total_time