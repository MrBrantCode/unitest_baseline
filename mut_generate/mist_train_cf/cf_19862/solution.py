"""
QUESTION:
Calculate the number of weekdays from a start date to an end date, excluding weekends and public holidays on weekdays.

The function, `count_weekdays`, should take in the following parameters: 
- `start_date` (datetime.date): The start date.
- `end_date` (datetime.date): The end date.
- `holidays` (list of datetime.date): A list of public holidays.

Restrictions: The function should not include weekends or public holidays in its count of weekdays.
"""

from datetime import date, timedelta

def count_weekdays(start_date, end_date, holidays):
    """
    Calculate the number of weekdays from a start date to an end date, 
    excluding weekends and public holidays on weekdays.

    Parameters:
    start_date (datetime.date): The start date.
    end_date (datetime.date): The end date.
    holidays (list of datetime.date): A list of public holidays.

    Returns:
    int: The number of weekdays.
    """

    # Initialize the count of weekdays
    weekdays = 0

    # Iterate over each day in the date range
    current_date = start_date
    while current_date <= end_date:
        # Check if the day is a weekday and not a public holiday
        if current_date.weekday() < 5 and current_date not in holidays:
            # Increment the count of weekdays
            weekdays += 1
        # Move to the next day
        current_date += timedelta(days=1)

    # Return the total count of weekdays
    return weekdays