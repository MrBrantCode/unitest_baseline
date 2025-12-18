"""
QUESTION:
Write a function `count_leap_year_days` that takes two parameters: `start_year` and `end_year`. The function should calculate and return the total number of days in the range of years from `start_year` to `end_year` (inclusive), considering leap years. A leap year occurs every 4 years, except for years that are divisible by 100 but not divisible by 400. The function should work efficiently for large ranges of years. The input years will be between 1 and 9999.
"""

def count_leap_year_days(start_year, end_year):
    total_days = 0
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            total_days += 366
        else:
            total_days += 365
    return total_days