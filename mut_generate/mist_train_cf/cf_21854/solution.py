"""
QUESTION:
Create a function `convert_gmt_to_local` that takes two parameters: `gmt_time` (a string representing a time in GMT format, e.g., "YYYY-MM-DD HH:MM:SS") and `time_zone` (a string representing a time zone, e.g., "America/New_York"). The function should return a string representing the corresponding local time in the specified time zone, accounting for daylight saving time (DST) if applicable. The function should handle time zones with non-whole hour offsets and should be able to handle dates within a reasonable range (e.g., from 1900 to 2100).
"""

import datetime
import pytz

def convert_gmt_to_local(gmt_time, time_zone):
    """
    Converts a given GMT time to the corresponding local time in the specified time zone, 
    accounting for daylight saving time (DST) if applicable.

    Args:
        gmt_time (str): A string representing a time in GMT format, e.g., "YYYY-MM-DD HH:MM:SS".
        time_zone (str): A string representing a time zone, e.g., "America/New_York".

    Returns:
        str: A string representing the corresponding local time in the specified time zone.
    """
    gmt_datetime = datetime.datetime.strptime(gmt_time, "%Y-%m-%d %H:%M:%S")
    gmt_timezone = pytz.timezone('GMT')
    gmt_aware_datetime = gmt_timezone.localize(gmt_datetime)

    local_timezone = pytz.timezone(time_zone)
    local_aware_datetime = gmt_aware_datetime.astimezone(local_timezone)

    return local_aware_datetime.strftime("%Y-%m-%d %H:%M:%S")