"""
QUESTION:
Write a function named `count_weekdays` that takes two string arguments representing dates in 'YYYY-MM-DD' format, calculates the number of weekdays (Monday to Friday) between the two given dates, and returns the result as an integer. The function should also implement error handling for invalid date inputs and account for leap years when calculating the number of weekdays. If the input dates are invalid or the date range is invalid, the function should return an error message.
"""

import datetime

def count_weekdays(date1, date2):
    """
    Calculate the number of weekdays (Monday to Friday) between two dates.

    Args:
        date1 (str): The start date in 'YYYY-MM-DD' format.
        date2 (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        int: The number of weekdays between the two dates.
        str: An error message if the input dates are invalid or the date range is invalid.
    """
    try:
        start_date = datetime.datetime.strptime(date1, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(date2, '%Y-%m-%d')
    except ValueError:
        return 'Invalid date format'

    if start_date > end_date:
        return 'Invalid date range'

    weekdays = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:
            weekdays += 1
        current_date += datetime.timedelta(days=1)

    return weekdays