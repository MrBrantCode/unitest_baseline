"""
QUESTION:
Develop a function named `convert_time` that takes three parameters: `time_input`, `from_tz`, and `to_tz`. The `time_input` should be a string representing a time in the format `YYYY-MM-DD HH:MM:SS`. The `from_tz` and `to_tz` parameters should be strings representing the timezones to convert from and to, respectively. The function should convert the `time_input` from the `from_tz` timezone to the `to_tz` timezone, accounting for daylight saving time, and return the converted time.
"""

import datetime
import pytz

def convert_time(time_input: str, from_tz: str, to_tz: str):
    from_tz_obj = pytz.timezone(from_tz)
    to_tz_obj = pytz.timezone(to_tz)

    naive_datetime_obj = datetime.datetime.strptime(time_input, "%Y-%m-%d %H:%M:%S")
    from_tz_datetime_obj = from_tz_obj.localize(naive_datetime_obj)
    
    to_tz_datetime_obj = from_tz_datetime_obj.astimezone(to_tz_obj)
    
    return to_tz_datetime_obj