"""
QUESTION:
Write a function called `calculate_bounces` that takes two parameters: `bounces_per_interval` and `interval_length` for the initial interval, as well as `total_time` to calculate the total number of bounces over a longer interval of time. The function should return the approximate number of bounces over the given total time. The input intervals are in seconds.
"""

def calculate_bounces(bounces_per_interval, interval_length, total_time):
    """
    Calculate the approximate number of bounces over a longer interval of time.

    Args:
        bounces_per_interval (int): The number of bounces per interval.
        interval_length (int): The length of the interval in seconds.
        total_time (int): The total time in seconds.

    Returns:
        int: The approximate number of bounces over the given total time.
    """
    bounce_rate = bounces_per_interval / interval_length  # bounces per second
    number_of_bounces = bounce_rate * total_time
    return round(number_of_bounces)