"""
QUESTION:
Create a function `is_leap_year(year)` that determines whether a given year is a leap year or not. A leap year is a year that is divisible by 4, but not divisible by 100 unless it is also divisible by 400. Implement the logic for determining whether a year is a leap year using bitwise operators. The input year should be a positive integer between 1000 and 9999 (inclusive). 

Implement the following features in the program: 
- Validate the input to ensure it is a positive integer between 1000 and 9999 (inclusive).
- Handle any invalid input gracefully by displaying an appropriate error message and allowing the user to try again.
- Use error handling to handle any exceptions that may occur during execution.
- Implement recursion to allow the user to enter multiple years and get the leap year status for each one, until the user chooses to exit the program.
- Use a custom exception class to handle the specific error cases (invalid input, calculation errors, etc.).
- Implement unit tests to verify the correctness of the leap year calculation and the error handling.
"""

def is_leap_year(year):
    """
    Determine whether a given year is a leap year or not using bitwise operators.

    A leap year is a year that is divisible by 4, but not divisible by 100 unless it is also divisible by 400.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False