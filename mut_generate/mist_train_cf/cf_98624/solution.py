"""
QUESTION:
Write a function `max_walk_time` that calculates the maximum time taken by three friends to walk a certain distance. The function should take the distance and the speeds of the three friends as input parameters and return the maximum time taken by the three friends to complete the walk. The distance and speeds are in meters and meters per minute, respectively.
"""

def max_walk_time(distance, speed_friend1, speed_friend2, speed_friend3):
    """
    Calculate the maximum time taken by three friends to walk a certain distance.

    Args:
        distance (float): The distance to be walked in meters.
        speed_friend1 (float): The speed of the first friend in meters per minute.
        speed_friend2 (float): The speed of the second friend in meters per minute.
        speed_friend3 (float): The speed of the third friend in meters per minute.

    Returns:
        float: The maximum time taken by the three friends to complete the walk in minutes.
    """
    time_friend1 = distance / speed_friend1
    time_friend2 = distance / speed_friend2
    time_friend3 = distance / speed_friend3
    return max(time_friend1, time_friend2, time_friend3)