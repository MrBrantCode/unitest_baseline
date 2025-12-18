"""
QUESTION:
Write a function named `convert_day_to_date` that takes two parameters: `day_of_year` (1-366) and `year` (1582-present), and returns the corresponding date in the format DD-MMM-YYYY, accounting for leap years according to the Gregorian calendar rules. The function should return an error message for invalid `day_of_year` or `year` values.
"""

from datetime import datetime, timedelta

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def convert_day_to_date(day_of_year, year):
    if day_of_year < 1 or (day_of_year > 366 or (day_of_year == 366 and not is_leap_year(year))):
        return "Invalid day of the year"
    if year < 1582:
        return "Invalid year. Enter a year from 1582 onwards"
    date = datetime(year, 1, 1) + timedelta(day_of_year - 1)
    return date.strftime('%d-%b-%Y')