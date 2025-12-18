"""
QUESTION:
Write a function `convert_to_ist` that takes a time in 24-hour format and a time zone as input, and returns the time converted to IST (Indian Standard Time). The time zone can be BST (British Summer Time), EST (Eastern Standard Time), or PST (Pacific Standard Time). The function should use the pytz library to handle time zone conversions.
"""

from datetime import datetime
from pytz import timezone

def convert_to_ist(time, tz):
    """
    Converts a time in 24-hour format to IST (Indian Standard Time) from a given time zone.

    Args:
    time (str): Time in 24-hour format.
    tz (str): Time zone. Can be 'BST', 'EST', or 'PST'.

    Returns:
    str: Time in IST format.
    """
    formatted_time = datetime.strptime(time, '%H:%M:%S')
    if tz == "BST":
        bst = timezone('Europe/London')
        time = bst.localize(formatted_time)
    elif tz == "EST":
        est = timezone('US/Eastern')
        time = est.localize(formatted_time)
    elif tz == "PST":
        pst = timezone('US/Pacific')
        time = pst.localize(formatted_time)

    ist = timezone('Asia/Kolkata')
    return time.astimezone(ist).strftime('%H:%M:%S')