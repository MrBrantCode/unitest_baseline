"""
QUESTION:
Create a function named `is_leap_year` that takes a year as input and returns a boolean indicating whether the year is a leap year. The function should account for leap year calculation intricacies, including the rules that years divisible by 4 are leap years, unless they are also divisible by 100, in which case they are not leap years unless they are also divisible by 400. 

Additionally, create another function `display_leap_years` that takes a start year and an end year as input and prints out all the leap years within that range, separated by commas.
"""

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def display_leap_years(start_year, end_year):
    leap_years = [year for year in range(start_year, end_year + 1) if is_leap_year(year)]
    return ', '.join(map(str, leap_years))