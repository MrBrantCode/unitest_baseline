"""
QUESTION:
Create a function `average_time_of_day` that takes a list of datetime objects as input and returns the average time of day across all the datetime objects as a string in the format "HH:MM", rounded to the nearest minute. The input list will always contain at least one element.
"""

from typing import List
from datetime import datetime, timedelta

def average_time_of_day(datetimes: List[datetime]) -> str:
    total_seconds = sum(dt.hour * 3600 + dt.minute * 60 + dt.second for dt in datetimes)
    average_seconds = total_seconds // len(datetimes)

    average_time = str(timedelta(seconds=average_seconds))
    if len(average_time) < 8:  # If seconds are single digit, add leading zero
        average_time = "0" + average_time

    return average_time[-8:-3]  # Extract the "HH:MM" part from the timedelta string