"""
QUESTION:
Create a function called `count_sundays_on_first` that takes two parameters, `year_start` and `year_end`, representing a range of years. The function should return the total number of Sundays that fall on the first day of a month (excluding January and December) across all years in the given range.
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