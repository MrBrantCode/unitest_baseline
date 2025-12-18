"""
QUESTION:
Convert a time from GMT to Antarctica Palmer's local time, given that Antarctica Palmer is GMT -3, and consider the potential effect of daylight saving on the time zone difference.
"""

from datetime import datetime, timedelta

def convert_gmt_to_palmer(gmt_time):
    """
    Converts a time from GMT to Antarctica Palmer's local time.
    
    Parameters:
    gmt_time (datetime): The time in GMT.
    
    Returns:
    datetime: The time in Antarctica Palmer's local time.
    """
    palmer_offset = timedelta(hours=-3)
    palmer_time = gmt_time + palmer_offset
    return palmer_time