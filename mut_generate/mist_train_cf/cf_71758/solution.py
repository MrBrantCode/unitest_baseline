"""
QUESTION:
Create a function `calculate_weekdays(year, month)` that calculates the total number of weekdays in a specific month and year. The input `month` should be an integer between 1 and 12, and the function should consider Monday to Friday as weekdays.
"""

import calendar

def calculate_weekdays(year, month):
    weekday_count = 0
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        if calendar.weekday(year, month, day) < 5:  
            weekday_count += 1
    return weekday_count