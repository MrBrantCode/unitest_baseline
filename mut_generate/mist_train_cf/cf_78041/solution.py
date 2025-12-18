"""
QUESTION:
Write a function `find_day_and_julian` that takes a date in the format 'DDMMYYYY' and returns a tuple containing the day of the week (as a string) and the Julian date (day of the year) as an integer. The date can be in any year from 1600 to 2100, inclusive. If the input date is invalid, return 'Invalid Date'. The function should account for leap years.
"""

from datetime import datetime

def find_day_and_julian(date):
    try:
        d = datetime.strptime(date, '%d%m%Y')
    except ValueError:
        return 'Invalid Date'

    day_of_week = d.strftime('%A')
    julian_day = d.timetuple().tm_yday
    return day_of_week, julian_day