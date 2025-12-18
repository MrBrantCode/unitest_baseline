"""
QUESTION:
Write a function called `calculate_seconds_in_years` that takes a positive integer `years` as input. The function should calculate the total number of seconds in the given number of years, taking into account leap years, and return the total seconds along with the number of leap years within the given range of years. Assume a non-leap year has 365 days and a leap year has 366 days.
"""

def calculate_seconds_in_years(years):
    seconds_in_year = 365 * 24 * 60 * 60
    leap_years = sum([1 for year in range(1, years + 1) if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)])
    total_seconds = years * seconds_in_year + leap_years * 24 * 60 * 60
    return total_seconds, leap_years