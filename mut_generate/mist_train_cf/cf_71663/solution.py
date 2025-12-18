"""
QUESTION:
Create a function named `calculate_leap_years(year_start, year_end)` that takes two integer arguments representing the start and end years of a time span. The function should return a list of all leap years within the given time span. Additionally, create a function named `factorial(n)` that calculates the factorial of a given integer `n`. The time span should be inclusive of the start year but not necessarily the end year, and the year is a leap year if it is evenly divisible by 4, except for end-of-century years which must be divisible by 400. This means that in the year 2000 was a leap year, although 1900 was not.
"""

def calculate_leap_years(year_start, year_end):
    """
    Returns a list of leap years within the given time span (inclusive of start year, but not necessarily the end year).
    
    A year is a leap year if it is evenly divisible by 4, except for end-of-century years which must be divisible by 400.
    
    Parameters:
    year_start (int): The start year of the time span.
    year_end (int): The end year of the time span.
    
    Returns:
    list: A list of leap years within the given time span.
    """
    leap_years = []
    
    # Adjusts the year range to include the end year in the calculation
    year_end += 1
    
    for year in range(year_start, year_end):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years.append(year)
            
    return leap_years

def factorial(n):
    """
    Calculates the factorial of a given integer n.
    
    Parameters:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)