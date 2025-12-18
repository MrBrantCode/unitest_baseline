"""
QUESTION:
Write a function named `compare_dates` that takes two date objects with millisecond level precision as input. The function should be able to handle timezones, leap years, and DST transitions correctly. It should return a string indicating whether the first date is equal to, greater than, or less than the second date. The function should convert the second date to the timezone of the first date if they are not the same.
"""

from datetime import datetime
from pytz import timezone

def compare_dates(date1, date2):
    """
    Compares two dates.
    
    Arguments:
    date1 -- First date.
    date2 -- Second date.
    
    Returns:
    Message about the date comparison.
    """
    # Check if the dates are in the same timezone, 
    # if not convert date2 to the timezone of date1
    if date1.tzinfo != date2.tzinfo:
        date2 = date2.astimezone(date1.tzinfo)

    # Compare the two dates
    if date1 == date2:
        return "Both dates are equal"
    elif date1 > date2:
        return "Date1 is greater than Date2"
    else:
        return "Date1 is less than Date2"