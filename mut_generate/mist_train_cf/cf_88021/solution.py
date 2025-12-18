"""
QUESTION:
Design a function named `print_leap_years` that takes two parameters: `start_year` and `end_year`, representing the interval between which to find leap years. The function should only consider years between 1600 and 3000, inclusive, and `start_year` must be before `end_year`. A year is considered a leap year if it is divisible by 4 but not by 100, unless it is also divisible by 400. The function should print all leap years within the given interval and the total number of leap years.
"""

def print_leap_years(start_year, end_year):
    # Validate input
    if start_year >= end_year:
        print("Invalid input: starting year must be before the ending year.")
        return
    if start_year < 1600 or end_year > 3000:
        print("Invalid input: the interval must be between the years 1600 and 3000.")
        return

    leap_years = []
    count = 0

    for year in range(start_year, end_year + 1):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap_years.append(year)
            count += 1

    # Print leap years
    print("Leap years between", start_year, "and", end_year, "are:", leap_years)
    print("Total number of leap years:", count)