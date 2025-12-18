"""
QUESTION:
Write a function julian_to_gregorian(julian_date_str) that takes a date in the form of a string (YYYY-MM-DD) and calculates the corresponding Gregorian date using the Julian calendar system. If the date is on or after October 15, 1582, the function should return the Gregorian date in the same string format, taking into account the 10-day shift that occurred during the Julian to Gregorian transition.
"""

from datetime import datetime, timedelta

def julian_to_gregorian(julian_date_str):
    julian_date = datetime.strptime(julian_date_str, '%Y-%m-%d')
    
    if julian_date.year > 1582 or (julian_date.year == 1582 and (julian_date.month > 10 or (julian_date.month == 10 and julian_date.day > 4))):
        gregorian_date = julian_date + timedelta(days=10)
    else:
        gregorian_date = julian_date
    
    return gregorian_date.strftime('%Y-%m-%d')