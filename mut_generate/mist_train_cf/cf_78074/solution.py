"""
QUESTION:
Write a function `weekdays_in_month` that takes a list of national holidays as input in the format "DD-MM-YYYY" and returns the number of remaining weekdays in the current month, excluding the given holidays. The function should handle the case where the current day is a holiday. The function should also account for the fact that all holidays will fall on a weekday.
"""

from datetime import date
import calendar

def weekdays_in_month(holidays):
    """
    Returns the number of remaining weekdays in the current month, excluding the given holidays.

    Args:
        holidays (list): A list of national holidays in the format "DD-MM-YYYY".

    Returns:
        int: The number of remaining weekdays in the current month.
    """

    today = date.today()
    month = today.month
    year = today.year

    last_day_of_month = max(calendar.monthcalendar(year, month)[-1])

    # Get the number of weekdays in the current month, excluding holidays
    weekdays = [day for day in range(today.day, last_day_of_month + 1) 
                if (calendar.weekday(year, month, day) < 5) 
                and (date(year, month, day).strftime("%d-%m-%Y") not in holidays)]

    return len(weekdays)