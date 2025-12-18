"""
QUESTION:
Write a function `get_weekday(day, month, year)` that takes three integers representing a date and returns the day of the week as a string. The function should return one of the following options: {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}. The input dates will always be valid and fall within the years 1971 and 2100.
"""

import datetime

def get_weekday(day, month, year):
    date = datetime.datetime(year, month, day)
    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return weekdays[date.weekday()]