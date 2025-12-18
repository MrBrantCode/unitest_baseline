"""
QUESTION:
Create a function `ordinal_date` that takes a string `date` representing a date in the Gregorian calendar, formatted as `YYYY-MM-DD`, and returns the ordinal day of the year. The string `date` should be exactly 10 characters long, with hyphens at the 5th and 8th positions, and should represent a valid calendar date between January 1st, 1900 and December 31, 2019.
"""

from datetime import datetime

def ordinal_date(date):
    date_time_obj = datetime.strptime(date, '%Y-%m-%d')
    return date_time_obj.timetuple().tm_yday