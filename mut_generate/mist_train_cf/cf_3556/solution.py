"""
QUESTION:
Design a function `print_leap_years` that takes two integer parameters, `start_year` and `end_year`, and prints all the leap years within the given interval, excluding years divisible by 100 but not by 400. The interval must be between 1600 and 3000, and `start_year` must be less than `end_year`. The function should also print the total number of leap years within the interval.
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