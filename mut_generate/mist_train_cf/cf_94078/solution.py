"""
QUESTION:
Create a function called `weekdays_in_year(year)` that takes an integer `year` as input and returns a list of all weekdays (Monday to Friday) in the given year, excluding New Year's Day (January 1st) and Christmas Day (December 25th). The function should return the list of dates in ascending order.
"""

import datetime
import calendar

def weekdays_in_year(year):
    weekdays = []
    holidays = [
        (1, 1),   # New Year's Day
        (12, 25), # Christmas Day
        # Add more holidays here...
    ]

    for month in range(1, 13):
        first_day = calendar.monthrange(year, month)[0]
        last_day = calendar.monthrange(year, month)[1]

        for day in range(1, last_day + 1):
            date = datetime.date(year, month, day)

            if date.weekday() < 5 and (month, day) not in holidays:
                weekdays.append(date)

    return sorted(weekdays)