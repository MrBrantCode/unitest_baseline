"""
QUESTION:
Create a function `get_weekdays(year, month)` that takes a year and month as input and returns a dictionary where keys are days of the week and values are counts of these days in the given month. The function should account for leap years.
"""

import calendar

def get_weekdays(year, month):
    # days in month
    days_in_month = calendar.monthrange(year, month)[1]
    weekdays = {calendar.day_name[i]: 0 for i in range(7)}
    
    for day_number in range(1, days_in_month + 1):
        day = calendar.weekday(year, month, day_number)
        weekdays[calendar.day_name[day]] += 1
   
    return weekdays