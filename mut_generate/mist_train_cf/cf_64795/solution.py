"""
QUESTION:
Create a function `julian_to_date(year, julian_day)` that takes a year and a Julian day of the year as input and returns the corresponding date in the format DD-MMM-YYYY. The function should validate the input, considering leap years and common years, and return an error message for invalid inputs. The function should work for any year, not just 2020. The year must be a positive integer, and the Julian day must be an integer between 1 and 366, inclusive.
"""

from datetime import datetime, timedelta

def julian_to_date(year, julian_day):
    # Validation
    if not isinstance(year, int) or not isinstance(julian_day, int):
        return 'Error: both year and julian_day must be integers'
    if year < 1:
        return 'Error: year must be positive'
    if julian_day < 1 or julian_day > 366:
        return 'Error: julian_day must be within 1-366'
    if julian_day == 366 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
        return f'Error: year {year} is not a leap year and does not have 366 days'

    # Process
    date = datetime(year, 1, 1) + timedelta(julian_day - 1)
    return date.strftime('%d-%b-%Y')