"""
QUESTION:
Create a function called `find_day_month_year` that takes two parameters, `year` and `month`, and determines the number of days in the given month and year, as well as the day of the week of the first and last day of the given month. The function should handle leap years and be valid for any input year within the range of 1900 and 2100.
"""

import calendar

def find_day_month_year(year, month):
    # Checking if the year is in the provided range
    if year < 1900 or year > 2100:
        return "Year should be in the range of 1900 and 2100."

    # Getting the number of days in a month and the day of the week of the first day
    week_day, num_days = calendar.monthrange(year, month)

    first_day = calendar.day_name[week_day]
    last_day = calendar.day_name[(week_day+num_days-1)%7]

    month_name = calendar.month_name[month]

    return f'{month_name} {year} has {num_days} days, the first day is {first_day}, and the last day is {last_day}.'