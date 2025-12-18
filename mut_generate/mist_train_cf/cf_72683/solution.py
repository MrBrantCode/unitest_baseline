"""
QUESTION:
Write a function `convert_time_to_date` that takes an integer `time` representing the number of hours since the beginning of the year (0-8760) and returns a string representing the corresponding date and hour in the format DD-MMM-YYYY HH:MM, assuming the year is 2020 and each day has 24 hours.
"""

from datetime import datetime, timedelta

def convert_time_to_date(time):
    start_of_year = datetime(year=2020, month=1, day=1)
    delta = timedelta(hours=time)
    new_date = start_of_year + delta
    return new_date.strftime('%d-%b-%Y %H:%M')