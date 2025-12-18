"""
QUESTION:
Write a function called `get_day_name` that takes three integers representing day, month, and year as input and returns the corresponding day of the week as a string. The function should handle leap years and should not use any built-in date or calendar library functions. Implement the function using mathematical algorithms and conditional statements.
"""

def get_day_name(day, month, year):
    """
    Calculate the day of the week for a given date using Zeller's Congruence.

    Args:
        day (int): The day of the month.
        month (int): The month of the year.
        year (int): The year.

    Returns:
        str: The corresponding day of the week as a string.
    """
    if month < 3: 
        month += 12
        year -= 1
    
    h = (day + int((13 * (month + 1)) / 5) + year + int(year / 4) - int(year / 100) + int(year / 400)) % 7
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return days[h]