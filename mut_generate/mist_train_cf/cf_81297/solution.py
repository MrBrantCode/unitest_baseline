"""
QUESTION:
Write a function `convert_to_12_hour` that takes a string representing time in 24-hour military format and returns its equivalent in 12-hour format with AM/PM suffix. The input string is in the format 'HH:MM' where 'HH' is the hour (00-23) and 'MM' is the minute (00-59).
"""

from datetime import datetime

def convert_to_12_hour(time_str):
    """
    Convert a time string from 24-hour military format to 12-hour format with AM/PM suffix.
    
    Args:
        time_str (str): Time in 24-hour military format (HH:MM)
    
    Returns:
        str: Time in 12-hour format with AM/PM suffix
    """
    time_obj = datetime.strptime(time_str, '%H:%M')
    return time_obj.strftime('%I:%M %p')