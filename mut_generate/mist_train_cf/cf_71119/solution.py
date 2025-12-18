"""
QUESTION:
Write a function `calculate_time_diff` that takes a list of two date and time values in the format '%Y-%m-%dT%H:%M:%S' as input, calculates the gap between the two dates in years, months, days, hours, minutes, and seconds, and returns the result as a list of six integers. The function should handle edge cases where the start date is more recent than the end date or where the two dates are the same.
"""

from dateutil.relativedelta import relativedelta
import datetime

def calculate_time_diff(date1, date2):
    """
    Calculate the time difference between two dates.

    Args:
        date1 (str): The first date in the format '%Y-%m-%dT%H:%M:%S'.
        date2 (str): The second date in the format '%Y-%m-%dT%H:%M:%S'.

    Returns:
        list: A list of six integers representing the time difference in years, months, days, hours, minutes, and seconds.
    """

    start_datetime = datetime.datetime.strptime(date1, '%Y-%m-%dT%H:%M:%S')
    end_datetime = datetime.datetime.strptime(date2, '%Y-%m-%dT%H:%M:%S')

    # Handle edge case where start_datetime is more recent than end_datetime
    if start_datetime > end_datetime:
        temp = start_datetime
        start_datetime = end_datetime
        end_datetime = temp

    rd = relativedelta(end_datetime, start_datetime)  

    return [rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds]