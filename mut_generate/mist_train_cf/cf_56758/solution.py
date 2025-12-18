"""
QUESTION:
Write a function `total_elapsed_days` that takes two dates as input and returns the total number of days elapsed between the start date 'January 1st, 1971' and the given end date, considering leap years.
"""

from datetime import datetime

def total_elapsed_days(end_date):
    """
    Calculate the total number of days elapsed between the start date 'January 1st, 1971' and the given end date.
    
    Args:
        end_date (str or datetime): The end date in 'YYYY-MM-DD' format or datetime object.
        
    Returns:
        int: The total number of days elapsed.
    """
    start_date = datetime(1971, 1, 1)
    
    # Convert end_date to datetime object if it's a string
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        
    difference = end_date - start_date
    
    return difference.days