"""
QUESTION:
Write a function `convert_datetime` that takes two string parameters, `date_string` and `format_string`. The `date_string` should be in the format "dd/mm/yyyy hh:mm:ss" and the `format_string` should be in the format "dd mm, yyyy hh:mm:ss" where "dd" represents the day of the month, "mm" represents the month, "yyyy" represents the year, "hh" represents the hour, "mm" represents the minute, and "ss" represents the second. The function should return the `date_string` in the specified `format_string`. The function should raise a `ValueError` if the `date_string` or the `format_string` is invalid.
"""

import datetime

def convert_datetime(date_string, format_string):
    """
    Converts a given DateTime string to the specified format.

    Args:
        date_string (str): The DateTime string to convert. It should be in the format "dd/mm/yyyy hh:mm:ss".
        format_string (str): The format to convert the DateTime string to.

    Returns:
        str: The DateTime string in the specified format.

    Raises:
        ValueError: If the date_string or the format_string is invalid.
    """
    # Convert the given DateTime string to a datetime object
    given_datetime_obj = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
    
    # Convert the datetime object to the specified format
    formatted_datetime_str = given_datetime_obj.strftime(format_string)
    
    return formatted_datetime_str