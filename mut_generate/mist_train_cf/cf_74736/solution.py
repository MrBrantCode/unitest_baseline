"""
QUESTION:
Create a function `day_to_date` that takes two parameters: `day` (an integer representing the day of the year, ranging from 1 to 366) and `utc_offset` (an integer representing the UTC offset in hours, ranging from -12 to 14). The function should return a date string in the format "DD-MMM-YYYY" corresponding to the given day of the year 2020, taking into account leap years and adjusting for the provided UTC offset.
"""

from datetime import datetime, timedelta

def day_to_date(day, utc_offset):
    date = datetime(2020, 1, 1)
    date += timedelta(days=day-1)
    date += timedelta(hours=utc_offset)
    return date.strftime('%d-%b-%Y')