"""
QUESTION:
Write a function named `convert_to_timestamp` that accepts a list of dates in the format "yyyy-mm-dd hh:mm:ss" and returns a dictionary where the keys are the input dates and the values are the corresponding timestamps in the UTC timezone. The function should handle leap years and time zones accurately.
"""

import datetime
import pytz

def convert_to_timestamp(dates):
    timestamps = {}
    utc_timezone = pytz.timezone('UTC')

    for date in dates:
        try:
            year, month, day, hour, minute, second = map(int, date.split(' ')[0].split('-') + date.split(' ')[1].split(':'))
            local_datetime = datetime.datetime(year, month, day, hour, minute, second)
            utc_datetime = utc_timezone.localize(local_datetime)
            timestamp = int(utc_datetime.timestamp())
            timestamps[date] = timestamp
        except:
            timestamps[date] = 'Invalid date format'

    return timestamps