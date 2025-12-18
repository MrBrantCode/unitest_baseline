"""
QUESTION:
Write a function named `find_day_of_week` that takes a date string in the format "dd/mm/yyyy" and returns the day of the week for the given date. The function should not take any arguments other than the date string. The date string should be parsed to extract the day, month, and year. The function should use the datetime module to find the day of the week.
"""

from datetime import datetime

def find_day_of_week(date_string):
    """
    This function takes a date string in the format "dd/mm/yyyy" and returns the day of the week for the given date.
    
    Parameters:
    date_string (str): A date string in the format "dd/mm/yyyy"
    
    Returns:
    str: The day of the week for the given date
    """
    day, month, year = date_string.split("/")
    date = datetime(int(year), int(month), int(day))
    return date.strftime("%A")