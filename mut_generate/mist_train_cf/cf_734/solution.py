"""
QUESTION:
Create a function `convert_datetime_to_string` that takes a `datetime_object`, `date_format`, and `time_format` as input and returns the formatted date and time as a string. The `date_format` should be a string representing the desired date format and the `time_format` should be a string representing the desired time format. The function should handle both 12-hour and 24-hour time formats.
"""

from datetime import datetime

def convert_datetime_to_string(datetime_object, date_format, time_format):
    """
    Converts a datetime object to a string based on the provided date and time formats.

    Args:
    - datetime_object (datetime): The datetime object to be converted.
    - date_format (str): The desired date format.
    - time_format (str): The desired time format.

    Returns:
    - str: The formatted date and time as a string.
    """
    formatted_date = datetime_object.strftime(date_format)
    formatted_time = datetime_object.strftime(time_format)
    return formatted_date + " " + formatted_time