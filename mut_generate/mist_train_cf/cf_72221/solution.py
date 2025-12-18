"""
QUESTION:
Given two times, one for Mike's finish time and the other being the difference in time between Mike and Joe's finish times, create a function called 'joe_finish_time' that returns the exact time Joe completed the marathon run.
"""

from datetime import datetime, timedelta

def joe_finish_time(mike_time, time_diff):
    """
    Calculate Joe's finish time based on Mike's finish time and the time difference.

    Args:
        mike_time (str): Mike's finish time in 'HH:MM' format.
        time_diff (int): Time difference in minutes between Mike and Joe's finish times.

    Returns:
        str: Joe's finish time in 'HH:MM' format.
    """
    # Convert Mike's time to datetime object
    mike_time = datetime.strptime(mike_time, '%I:%M %p')

    # Subtract the time difference from Mike's time to get Joe's time
    joe_time = mike_time - timedelta(minutes=time_diff)

    # Convert Joe's time back to string and return
    return joe_time.strftime('%I:%M %p')