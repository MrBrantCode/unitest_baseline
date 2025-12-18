"""
QUESTION:
Write a function `calculate_weekdays` that calculates the number of weekdays taken to finish a task given its start and end dates. The function should exclude weekends (Saturday and Sunday) and return the number of weekdays. If the number of weekdays exceeds 30, it should return the total number of weekdays, even if it's more than the maximum allowed duration. The start date and end date should be passed as input to the function in the format 'DD MM YYYY'.
"""

from datetime import datetime, timedelta

def calculate_weekdays(start_date, end_date):
    """
    Calculate the number of weekdays between two dates.

    Args:
    start_date (str): The start date in the format 'DD MM YYYY'.
    end_date (str): The end date in the format 'DD MM YYYY'.

    Returns:
    int: The number of weekdays between the start and end dates.
    """

    # Convert the input strings to datetime objects
    start_date = datetime.strptime(start_date, '%d %m %Y')
    end_date = datetime.strptime(end_date, '%d %m %Y')

    # Calculate the total number of days between the start and end dates
    total_days = (end_date - start_date).days + 1

    # Initialize the number of weekdays
    weekdays = 0

    # Iterate over each day between the start and end dates
    for n in range(total_days):
        # Calculate the current date
        current_date = start_date + timedelta(n)

        # Check if the current date is a weekday
        if current_date.weekday() < 5:
            # If it's a weekday, increment the count
            weekdays += 1

    # Return the total number of weekdays
    return weekdays