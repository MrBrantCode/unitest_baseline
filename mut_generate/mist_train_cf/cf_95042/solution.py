"""
QUESTION:
Write a function `count_sundays_on_first` that takes two integers `year_start` and `year_end` as input and returns the number of Sundays that fall on the first of a month, excluding January and December, for each year in the given range from `year_start` to `year_end`.
"""

import datetime

def count_sundays_on_first(year_start, year_end):
    count = 0
    for year in range(year_start, year_end + 1):
        for month in range(2, 12):  # Excluding January and December
            date = datetime.date(year, month, 1)
            if date.weekday() == 6:  # Sunday is represented by 6 in the weekday() function
                count += 1
    return count