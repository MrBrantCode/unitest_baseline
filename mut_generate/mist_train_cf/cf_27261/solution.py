"""
QUESTION:
Create a function `count_weekdays_between_timestamps` that takes a sorted list of pandas Timestamp objects and a timezone as input. The function should return the total count of weekdays (excluding Saturdays and Sundays) between each consecutive pair of timestamps in the specified timezone. The input list of timestamps is guaranteed to have at least two elements.
"""

from pandas import Timestamp, DateOffset, to_datetime
import pandas as pd

def count_weekdays_between_timestamps(timestamps, timezone):
    weekdays_count = 0
    for i in range(len(timestamps) - 1):
        start_date = to_datetime(timestamps[i].tz_convert(timezone).date())
        end_date = to_datetime(timestamps[i + 1].tz_convert(timezone).date())
        date_range = pd.date_range(start=start_date, end=end_date, freq='B')
        weekdays_count += len(date_range)
    return weekdays_count