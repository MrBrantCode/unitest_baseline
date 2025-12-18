"""
QUESTION:
Write a function `convert_time_to_zone` that takes a UTC timezone (in the format of IANA Time Zone Database) as input, converts the current Japan Standard Time to the specified UTC timezone, and returns the current time in the target timezone, handling daylight saving changes where applicable.
"""

import datetime
import pytz

def convert_time_to_zone(zone):
    japan_time = datetime.datetime.now(pytz.timezone('Japan'))
    target_time = japan_time.astimezone(pytz.timezone(zone))
    return target_time