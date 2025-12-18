"""
QUESTION:
Write a function named `calculate_seconds` that calculates the total number of seconds in a given number of years, taking into account leap years, and returns the total number of seconds along with the number of leap years. The function should assume that the input is a positive integer.
"""

def calculate_seconds(years):
    seconds_per_year = 365 * 24 * 60 * 60
    leap_years = sum([1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0 for year in range(1, years+1)])
    total_seconds = years * seconds_per_year + leap_years * 24 * 60 * 60
    return total_seconds, leap_years