"""
QUESTION:
Design a function called `convert_timestamp` that takes two parameters: `epoch_time` and `target_tz`. The function should translate the provided Unix timestamp (`epoch_time`) into a human-readable date/time format in the specified `target_tz` timezone. The function should handle both positive and negative epoch times and support various timezones, including GMT and PST (which should be represented as 'US/Pacific'). 

The function should return the converted date/time as a string in the '%Y-%m-%d %H:%M:%S' format. The function should utilize the `pytz` module for handling timezone conversions and should not use the `timedelta` function for timezone conversions.
"""

from datetime import datetime
from pytz import timezone

def convert_timestamp(epoch_time, target_tz):
    """Translate epoch time to a specified timezone"""
    utc_time = datetime.utcfromtimestamp(epoch_time)
    target_time = utc_time.astimezone(timezone(target_tz))
    return target_time.strftime('%Y-%m-%d %H:%M:%S')