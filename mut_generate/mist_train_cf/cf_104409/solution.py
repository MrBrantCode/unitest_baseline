"""
QUESTION:
Create a function named `get_day_of_week` that takes a string `date_string` representing a date in the format "dd/mm/yyyy" and returns the day of the week as a string. The function should handle leap years correctly.
"""

import datetime

def get_day_of_week(date_string):
    day, month, year = map(int, date_string.split('/'))
    date = datetime.date(year, month, day)
    day_of_week = date.strftime("%A")
    return day_of_week