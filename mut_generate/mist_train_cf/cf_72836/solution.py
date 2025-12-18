"""
QUESTION:
Write a function named `time_interval` that takes two timestamps in the format `%m/%d/%Y` and returns the time duration between them, inclusive of days, hours, minutes, and seconds. The function should compute the difference between the two dates and express it in terms of days, hours, minutes, and seconds. The time interval should be calculated as the difference between the two input timestamps.
"""

from datetime import datetime

def time_interval(date1, date2):
    """
    Compute the time duration between two timestamps in the format %m/%d/%Y.

    Args:
    date1 (str): The first timestamp.
    date2 (str): The second timestamp.

    Returns:
    str: The time duration between the two timestamps, inclusive of days, hours, minutes, and seconds.
    """

    # Define the date format
    date_format = "%m/%d/%Y"

    # Convert the dates to datetime objects
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)

    # Compute the difference between the dates
    delta = b - a

    # Compute the number of days, hours, minutes and seconds 
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds // 60) % 60
    seconds = delta.seconds % 60

    # Return the result
    return "There are {} days, {} hours, {} minutes and {} seconds between the two dates.".format(days, hours, minutes, seconds)