"""
QUESTION:
Write a function `weekdays_in_year(year)` that takes a year as input and returns a list of all weekdays (Monday to Friday) in that year, excluding holidays. The function should consider the following holidays: New Year's Day (January 1st) and Christmas Day (December 25th). The returned list should be sorted in ascending order. The function should not take any additional inputs other than the year.
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