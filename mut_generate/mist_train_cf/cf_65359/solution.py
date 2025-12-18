"""
QUESTION:
Write a function named `time_difference` that calculates the difference between two `datetime.time` objects, `t1` and `t2`. The function should consider the case where `t1` and `t2` may span across midnight. The function should return a `datetime.timedelta` object representing the difference between `t1` and `t2`.
"""

from datetime import datetime, date, timedelta

def time_difference(t1, t2):
    """
    Calculate the difference between two datetime.time objects, considering the case 
    where they may span across midnight.

    Args:
    t1 (datetime.time): The first time object.
    t2 (datetime.time): The second time object.

    Returns:
    datetime.timedelta: The difference between t1 and t2.
    """
    dt1 = datetime.combine(date.today(), t1)
    dt2 = datetime.combine(date.today(), t2)

    # If dt1 is less than dt2, it means t1 is from the next day
    if dt1 < dt2:
        dt1 = dt1 + timedelta(days=1)

    diff = dt1 - dt2
    return diff