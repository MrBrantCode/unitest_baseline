"""
QUESTION:
Create a function named `is_leap_year` that takes an integer `year` as input and returns `True` if it's a leap year, `False` otherwise, following these rules:
- If the year is divisible by 4, check further.
- If the year is divisible by 100, it must also be divisible by 400 to be a leap year.
- Otherwise, it's a leap year if it's divisible by 4 but not by 100.

Write a program using the `is_leap_year` function that:
- Takes a range of years (start and end) as input from the user.
- Counts the number of leap years within this range.
- Calculates the average number of leap years per decade within the given range (rounded to two decimal places).
- Outputs the total number of leap years and the average number of leap years per decade.
"""

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False