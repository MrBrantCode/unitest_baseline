"""
QUESTION:
Write a function named `count_weekdays` that calculates the number of weekdays (Monday to Friday) between two given dates, considering leap years. The function should take two parameters, `date1` and `date2`, both in the format 'YYYY-MM-DD'. Implement error handling for invalid date inputs and ensure the function returns `None` if the input dates are invalid or if `date1` is later than `date2`.
"""

import datetime

def count_weekdays(date1, date2):
    """
    Calculate the number of weekdays (Monday to Friday) between two given dates.

    Args:
    date1 (str): The start date in 'YYYY-MM-DD' format.
    date2 (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    int or None: The number of weekdays between date1 and date2, or None if the input dates are invalid or date1 is later than date2.
    """
    
    try:
        start_date = datetime.datetime.strptime(date1, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(date2, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return None
    
    if start_date > end_date:
        print("Start date cannot be later than end date.")
        return None
    
    weekdays = 0
    current_date = start_date
    
    while current_date <= end_date:
        if current_date.weekday() < 5:  # Monday to Friday
            weekdays += 1
        current_date += datetime.timedelta(days=1)
    
    return weekdays