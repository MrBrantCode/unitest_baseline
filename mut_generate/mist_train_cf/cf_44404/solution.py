"""
QUESTION:
Write a function `find_day_of_week` that takes a list of the days of the week and the day of the week on which February 1st falls as input, and returns the day of the week on which April 1st falls, considering that February has 28 days and March has 31 days. The function should only use these two parameters and return the result as a string representing the day of the week.
"""

def find_day_of_week(days, start_day):
    """
    Calculate the day of the week on which April 1st falls.

    Args:
    days (list): A list of the days of the week.
    start_day (str): The day of the week on which February 1st falls.

    Returns:
    str: The day of the week on which April 1st falls.
    """
    total_days = 59
    index = (days.index(start_day) + total_days) % 7
    return days[index]