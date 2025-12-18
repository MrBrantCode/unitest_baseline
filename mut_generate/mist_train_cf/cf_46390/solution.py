"""
QUESTION:
Create a function called `print_calendar` that takes two parameters, `year` and `month`, and prints the calendar of the given month and year. The function should take into account leap years and prohibit inputs for dates before the year 1900. The month should be between 1 and 12.
"""

import calendar

def print_calendar(year, month):
    if year < 1900:
        print("Invalid input: Year should be greater than or equal to 1900.")
        return

    try:
        calendar.setfirstweekday(calendar.SUNDAY)
        print(calendar.month(year, month))
    except calendar.IllegalMonthError:
        print("Invalid input: Month should be between 1 and 12.")