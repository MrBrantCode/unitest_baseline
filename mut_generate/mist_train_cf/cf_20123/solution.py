"""
QUESTION:
Write a function named `compare_dates` that takes two `datetime` objects (`date1` and `date2`) and their respective time zones (`timezone1` and `timezone2`) as input. The function should compare the two dates after converting them to a common time zone, taking into account daylight saving time changes. It should return a string indicating whether `date1` is before, after, or the same as `date2`.
"""

import pytz
from datetime import datetime

def compare_dates(date1, date2, timezone1, timezone2):
    # Convert both dates to UTC timezone
    date1 = pytz.timezone(timezone1).localize(date1).astimezone(pytz.utc)
    date2 = pytz.timezone(timezone2).localize(date2).astimezone(pytz.utc)
    
    if date1 < date2:
        return "The first date is before the second date."
    elif date1 > date2:
        return "The first date is after the second date."
    else:
        return "Both dates are the same."