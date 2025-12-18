"""
QUESTION:
Create a function `convert_time` that takes a string `time` in the format 'YYYY-MM-DD HH:MM:SS', a string `from_timezone` representing the time zone of the given time, and a string `to_timezone` representing the target time zone for conversion. The function should return a datetime object representing the time in the `to_timezone` time zone. The time zones should be provided in the 'Area/City' format (e.g., 'America/New_York').
"""

from datetime import datetime
import pytz

def convert_time(time, from_timezone, to_timezone):
    datetime_obj_naive = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    
    from_tz = pytz.timezone(from_timezone)
    datetime_obj_aware = from_tz.localize(datetime_obj_naive)
    
    to_tz = pytz.timezone(to_timezone)
    new_datetime_obj = datetime_obj_aware.astimezone(to_tz)
    return new_datetime_obj