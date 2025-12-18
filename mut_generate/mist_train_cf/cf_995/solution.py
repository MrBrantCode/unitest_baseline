"""
QUESTION:
Write a function `calculate_total_days(start_year, end_year)` that takes two integers as input representing the start and end years, and returns the total number of days in the range of years, inclusive, considering leap years. The function should handle cases where the start year is greater than the end year and should be efficient for large ranges of years. The input years can range from -9999 to 9999.
"""

def calculate_total_days(start_year, end_year):
    if start_year > end_year:
        start_year, end_year = end_year, start_year

    total_days = 0
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            total_days += 366
        else:
            total_days += 365

    return total_days