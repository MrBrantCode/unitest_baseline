"""
QUESTION:
Write a function called `convert_berlin_time` that takes two parameters: `to_tz` (a string representing the target time zone in IANA time zone database format) and `berlin_time` (a datetime object representing the time in Berlin). The function should convert `berlin_time` to its equivalent in `to_tz`, handling daylight saving time adjustments, and return the converted time. The function should also handle invalid `to_tz` inputs by raising an exception. The function should assume that `berlin_time` is already localized to the 'Europe/Berlin' time zone.
"""

import pytz
from datetime import datetime

def convert_berlin_time(to_tz, berlin_time):
    berlin = pytz.timezone('Europe/Berlin')
    berlin_time = berlin.localize(berlin_time)
    to_tz = pytz.timezone(to_tz)
    to_tz_time = berlin_time.astimezone(to_tz)
    return to_tz_time