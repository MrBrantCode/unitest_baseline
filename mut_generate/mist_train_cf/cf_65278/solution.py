"""
QUESTION:
Create a function `get_date_range` that generates a sequence of dates and returns a row for every day/month/year even when no data is present in the given table. The function should take into account large date ranges and optimize for performance.
"""

from datetime import date, timedelta

def get_date_range(start_date: date, end_date: date) -> list:
    """
    Generates a sequence of dates from start_date to end_date.
    
    Args:
    start_date (date): The start date of the range.
    end_date (date): The end date of the range.
    
    Returns:
    list: A list of dates in the range.
    """
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    return dates