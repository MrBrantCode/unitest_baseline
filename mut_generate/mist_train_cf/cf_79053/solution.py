"""
QUESTION:
Create a function called `get_available_dates` that returns a list of dates in a given month that match a specified day of the week (e.g., all Mondays). The function should take two parameters: `year` and `month`, and return a list of dates in the specified month and year that match the specified day of the week. Assume the day of the week is Monday.
"""

import calendar
from datetime import date, timedelta

def get_available_dates(year, month):
    """
    Returns a list of dates in a given month that match a specified day of the week (e.g., all Mondays).

    Args:
        year (int): The year for which to get the dates.
        month (int): The month for which to get the dates.

    Returns:
        list: A list of dates in the specified month and year that match the specified day of the week.
    """
    # Get the first Monday in the month
    first_day = date(year, month, 1)
    while first_day.weekday() != 0:  # 0 represents Monday
        first_day += timedelta(days=1)

    # Get the last day of the month
    last_day = date(year, month, calendar.monthrange(year, month)[1])

    # Generate all Mondays in the month
    mondays = [first_day]
    current_day = first_day + timedelta(days=7)
    while current_day <= last_day:
        mondays.append(current_day)
        current_day += timedelta(days=7)

    return mondays