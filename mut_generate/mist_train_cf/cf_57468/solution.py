"""
QUESTION:
Write a function `convert_eastern_to_utc2` that takes a date and time in Eastern Standard Time (EST) or Eastern Daylight Time (EDT) as input and returns the equivalent time in UTC+2, considering daylight saving time transitions.
"""

from datetime import datetime
import pytz

def convert_eastern_to_utc2(est_time):
    """
    This function converts Eastern Standard Time (EST) or Eastern Daylight Time (EDT) to UTC+2.
    
    Parameters:
    est_time (datetime): A datetime object representing the time in EST or EDT.
    
    Returns:
    datetime: The equivalent time in UTC+2.
    """
    # First, we need to define the Eastern Time zone, which can be either EST or EDT
    eastern = pytz.timezone('US/Eastern')
    
    # Localize the input datetime object to Eastern Time zone
    eastern_time = eastern.localize(est_time)
    
    # Define the UTC+2 time zone
    utc2 = pytz.timezone('Etc/GMT-2')
    
    # Convert the Eastern Time to UTC+2
    utc2_time = eastern_time.astimezone(utc2)
    
    return utc2_time