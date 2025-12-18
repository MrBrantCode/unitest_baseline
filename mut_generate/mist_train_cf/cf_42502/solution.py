"""
QUESTION:
Implement the `get_day_of_week_utc_unix` function that takes a Unix timestamp `ts` as input and returns the day of the week in Coordinated Universal Time (UTC). The function must utilize two provided helper functions: `conv_unixts_to_utc_hms(ts)` which converts the Unix timestamp to UTC time in hours, minutes, and seconds, and `get_day_of_week(utc_time)` which returns the day of the week for a given UTC time. The `get_day_of_week_utc_unix` function should return the result as a string.
"""

import datetime

def get_day_of_week_utc_unix(ts: int) -> str:
    utc_time = datetime.datetime.utcfromtimestamp(ts)
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days_of_week[utc_time.weekday()]