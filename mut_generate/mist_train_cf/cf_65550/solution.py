"""
QUESTION:
Write a function `find_day` that takes a string date in 'yyyy-mm-dd' format as input and returns the corresponding day of the week as a string. The function should be able to handle any valid date in the Gregorian calendar.
"""

from datetime import datetime

def find_day(date: str) -> str:
    """ This function takes a date as a string in 'yyyy-mm-dd' format 
        and returns the day of the week.
    """

    date_format = datetime.strptime(date, '%Y-%m-%d')
    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                   'Friday', 'Saturday', 'Sunday']

    return day_of_week[date_format.weekday()]