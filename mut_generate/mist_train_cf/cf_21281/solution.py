"""
QUESTION:
Create a function `is_leap_year(year)` that takes a positive integer `year` as input and returns `True` if it is a leap year, `False` otherwise. The function must not use the modulo operator (`%`), built-in mathematical functions, loops, or recursion.
"""

def entrance(year):
    # Check if the year is divisible by 4
    is_divisible_by_4 = (year // 4) * 4 == year

    # Check if the year is divisible by 100
    is_divisible_by_100 = (year // 100) * 100 == year

    # Check if the year is divisible by 400
    is_divisible_by_400 = (year // 400) * 400 == year

    # A year is a leap year if it's divisible by 4 but not divisible by 100,
    # unless it's also divisible by 400
    return is_divisible_by_4 and (not is_divisible_by_100 or is_divisible_by_400)