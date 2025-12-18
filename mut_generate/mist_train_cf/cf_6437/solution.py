"""
QUESTION:
Write a function called `get_day_of_week` that takes three parameters - day, month, and year. The function should use Zeller's Congruence algorithm to calculate the day of the week for the given date. The input validation for day, month, and year should be done in the main part of the script. The `get_day_of_week` function should return the day of the week as an integer where 0 represents Saturday, 1 represents Sunday, and so on.
"""

def get_day_of_week(day, month, year):
    """
    Calculate the day of the week for the given date using Zeller's Congruence algorithm.
    
    Parameters:
    day (int): The day of the month (1-31)
    month (int): The month of the year (1-12)
    year (int): The year
    
    Returns:
    int: The day of the week as an integer where 0 represents Saturday, 1 represents Sunday, and so on.
    """
    if month == 1 or month == 2:
        month += 12
        year -= 1
    h = (day + (13 * (month + 1) // 5) + year + (year // 4) - (year // 100) + (year // 400)) % 7
    return h