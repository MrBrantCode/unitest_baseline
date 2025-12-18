"""
QUESTION:
Write a function called `convert_time_zones` that takes two parameters: `original_time` (a datetime object representing the current time in the Australian Eastern Standard Time zone), and `target_time_zones` (a list of time zone strings). The function should convert the original time to the target time zones and return the converted times along with information about whether daylight saving is active in both the original and target time zones. The target time zones should include 'Etc/GMT+1' (UTC-1), 'Etc/GMT-1' (UTC+1), and 'Etc/GMT-4' (UTC+4).
"""

from datetime import datetime
import pytz

def convert_time_zones(original_time, target_time_zones):
    """
    This function takes an original time in the Australian Eastern Standard Time zone and 
    a list of target time zones, and returns a dictionary with the converted times 
    along with information about whether daylight saving is active in both the original 
    and target time zones.

    Parameters:
    original_time (datetime): The original time in the Australian Eastern Standard Time zone.
    target_time_zones (list): A list of time zone strings.

    Returns:
    dict: A dictionary with the converted times and DST information.
    """

    # Get the original time zone
    original_tz = original_time.tzinfo

    # Initialize the result dictionary
    result = {}

    # Convert the time to each target time zone
    for tz_str in target_time_zones:
        tz = pytz.timezone(tz_str)
        converted_time = original_time.astimezone(tz)
        
        # Check if DST is active in both the original and target time zones
        original_dst = bool(original_time.dst())
        target_dst = bool(converted_time.dst())

        # Add the converted time and DST information to the result dictionary
        result[tz_str] = {
            'converted_time': converted_time,
            'original_dst': original_dst,
            'target_dst': target_dst
        }

    return result