"""
QUESTION:
Write a function named `days_in_month` that takes the year, month, and whether it is a leap year as inputs, and returns the number of days in the given month. The function should not rely on the day of the week of the first day of the month.
"""

def days_in_month(year, month, is_leap_year):
    """
    Returns the number of days in the given month.

    Parameters:
    year (int): The year.
    month (int): The month.
    is_leap_year (bool): Whether the year is a leap year.

    Returns:
    int: The number of days in the month.
    """
    
    # Define the number of days in each month for non-leap years
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # If it's a leap year, February has 29 days
    if is_leap_year:
        days_in_months[1] = 29
    
    # Return the number of days in the given month
    return days_in_months[month - 1]