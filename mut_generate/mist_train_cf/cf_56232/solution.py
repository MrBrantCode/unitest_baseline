"""
QUESTION:
Write a function named `convert_epoch_time` that takes an epoch time as input and returns the time in both UTC and the local time zone, as well as the difference between the two times. The function should not take any additional arguments.
"""

from datetime import datetime
import pytz

def convert_epoch_time(epoch_time):
    """
    This function converts epoch time to UTC and local time zone.

    Args:
    epoch_time (int): The time in epoch format.

    Returns:
    A tuple containing UTC time, local time, and their difference.
    """

    # Convert to UTC
    utc_time = datetime.utcfromtimestamp(epoch_time)
    
    # Convert to Local time zone
    local_time = datetime.fromtimestamp(epoch_time)

    # Calculate difference between two times
    time_diff = local_time - utc_time

    return utc_time, local_time, time_diff