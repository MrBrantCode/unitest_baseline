"""
QUESTION:
Create a function `find_sunrise_time` that takes a list of sunrise times and a target date as input, and returns the sunrise time for the given date in the format 'HH:MM AM/PM' if found, otherwise returns None. The sunrise times are in the format 'YYYY-MM-DD HH:MM:SS' and the target date is in the format 'YYYY-MM-DD'.
"""

import datetime

def find_sunrise_time(sunrise_times, target_date):
    """
    This function finds the sunrise time for a given date from a list of sunrise times.

    Args:
        sunrise_times (list): A list of sunrise times in the format 'YYYY-MM-DD HH:MM:SS'.
        target_date (str): The target date in the format 'YYYY-MM-DD'.

    Returns:
        str: The sunrise time for the given date in the format 'HH:MM AM/PM' if found, otherwise None.
    """
    # Convert sunrise times to datetime objects
    sunrise_times = [datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S') for t in sunrise_times]
    # Convert target date to datetime object
    target_date = datetime.datetime.strptime(target_date, '%Y-%m-%d')
    # Find the matching time
    matching_time = next((t for t in sunrise_times if t.date() == target_date.date()), None)
    # Return the matching time in the required format if found
    return matching_time.strftime('%I:%M %p') if matching_time else None