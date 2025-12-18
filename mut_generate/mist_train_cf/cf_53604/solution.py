"""
QUESTION:
Create a function `count_weekdays(year, month)` that takes an integer `year` and an integer `month` as input, and returns a dictionary where the keys are the names of the days of the week and the values are the number of times each day occurs in the given month and year. The function should correctly handle leap years.
"""

import calendar

def count_weekdays(year, month):
    # Create a calendar of the given month and year
    _calendar = calendar.monthcalendar(year, month)
    
    # Count the total number of weekdays in a month
    count = {n: sum(week[n] != 0 for week in _calendar) for n in range(7)}
    
    # Associate weekdays with their respective counts
    weekdays = {list(calendar.day_name)[n]: count[n] for n in range(7)}
    
    return weekdays