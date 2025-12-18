"""
QUESTION:
Write a function `count_leap_year_days` that calculates the total number of days in a given year range, considering leap years. The function should take two integers `start_year` and `end_year` as input, where 1 ≤ `start_year` ≤ 9999 and 1 ≤ `end_year` ≤ 9999, and return the total number of days in the range of years, inclusive. A leap year occurs every 4 years, except for years that are divisible by 100 but not divisible by 400.
"""

def count_leap_year_days(start_year, end_year):
    total_days = 0
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            total_days += 366
        else:
            total_days += 365
    return total_days