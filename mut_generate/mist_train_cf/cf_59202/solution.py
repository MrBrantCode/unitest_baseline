"""
QUESTION:
Write a function named `find_day_of_week` that takes a date string in the ISO 8601 standard format (YYYY-MM-DD) as input and returns the corresponding day of the week as a string. The function should use Python's built-in datetime library and return the day of the week with Monday as the first day (Monday = 0, Sunday = 6).
"""

import datetime

def find_day_of_week(date_string):
    """
    This function takes a date string in the ISO 8601 standard format (YYYY-MM-DD) 
    as input and returns the corresponding day of the week as a string.

    Args:
        date_string (str): A date string in the ISO 8601 standard format.

    Returns:
        str: The day of the week corresponding to the input date.
    """

    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return day_of_week_list[date_object.weekday()]