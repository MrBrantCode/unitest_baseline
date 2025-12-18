"""
QUESTION:
Write a function `convert_to_local_time` that takes two parameters: `gmt_time_str` (a string representing time in GMT format) and `local_tz_str` (a string representing the local timezone). The function should convert the given GMT time to the local time, taking into account daylight savings and standard time. Assume the input GMT time string is in the format '%Y-%m-%d %H:%M:%S'.
"""

from datetime import datetime
import pytz 

def convert_to_local_time(gmt_time_str, local_tz_str):
    gmt = pytz.timezone('GMT')
    local_tz = pytz.timezone(local_tz_str)

    # Parse the GMT time, and set its timezone to GMT
    gmt_time = datetime.strptime(gmt_time_str, '%Y-%m-%d %H:%M:%S')
    gmt_time = gmt.localize(gmt_time)

    # Convert to local timezone
    return gmt_time.astimezone(local_tz)