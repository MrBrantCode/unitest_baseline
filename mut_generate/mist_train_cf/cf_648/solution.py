"""
QUESTION:
Write a function named `get_day_of_week` that takes a string representing a date in the "yyyy-mm-dd" format as input and returns the day of the week corresponding to that date. The function should handle both past and future dates. The implementation should only use built-in Python libraries and should not make use of any external modules or libraries. The function should also handle invalid input dates, such as dates with incorrect formats, by returning an error message.
"""

import datetime

def entance(date_string):
    try:
        year, month, day = map(int, date_string.split("-"))
        date = datetime.date(year, month, day)
        day_of_week = date.strftime("%A")
        return day_of_week
    except ValueError:
        return "Invalid date format. Please use 'yyyy-mm-dd'."