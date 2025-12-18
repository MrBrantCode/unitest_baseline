"""
QUESTION:
Write a function `calculate_max_time` that takes in the speed of three friends and the distance they need to walk, and returns the maximum time taken among the friends to complete the walk. The speed is given in meters per minute and the distance is given in meters. The function should return the maximum time in minutes.
"""

def calculate_max_time(speed1, speed2, speed3, distance):
    """
    Calculate the maximum time taken among three friends to complete a walk.

    Args:
        speed1 (float): Speed of the first friend in meters per minute.
        speed2 (float): Speed of the second friend in meters per minute.
        speed3 (float): Speed of the third friend in meters per minute.
        distance (float): Distance to be covered in meters.

    Returns:
        float: Maximum time taken among the three friends in minutes.
    """
    # calculate time taken by each friend to complete the walk
    time1 = distance / speed1
    time2 = distance / speed2
    time3 = distance / speed3

    # find the maximum time taken among the three friends
    max_time = max(time1, time2, time3)

    return max_time