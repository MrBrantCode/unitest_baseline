"""
QUESTION:
Create a function `convert_timezone` that takes a list of datetime objects in 'Asia/Kolkata' timezone and a target timezone name as input, and returns a list of datetime objects in the target timezone. The function should account for daylight saving time and return an error message if the target timezone is invalid.
"""

import pytz
from datetime import datetime

def convert_timezone(ist_timestamps, tz_name):
    if tz_name in pytz.all_timezones:
        ist = pytz.timezone('Asia/Kolkata')
        target_tz = pytz.timezone(tz_name)
        converted_timestamps = []

        for ts in ist_timestamps:
            target_time = ts.astimezone(target_tz)
            converted_timestamps.append(target_time)

        return converted_timestamps 
    else:
        return 'Invalid timezone'