"""
QUESTION:
Design a function `print_leap_years(start_year, end_year)` that prints all the leap years within a given interval from `start_year` to `end_year` (inclusive), excluding years that are divisible by 100 but not by 400. The interval must be between 2000 and 2100, and `start_year` must be before `end_year`.
"""

def print_leap_years(start_year, end_year):
    if start_year >= end_year:
        print("Starting year must be before the ending year.")
        return
    
    if start_year < 2000 or end_year > 2100:
        print("Interval must be between the years 2000 and 2100.")
        return
    
    leap_years = []
    for year in range(start_year, end_year + 1):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap_years.append(year)
    
    print("Leap years within the interval:", leap_years)