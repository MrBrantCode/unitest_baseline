"""
QUESTION:
Write a function called `convert_datetime_format` that takes two string parameters: `datetime_str` and `format_str`. The `datetime_str` parameter should be in the format "dd/mm/yyyy hh:mm:ss" and the `format_str` parameter should be a valid format string for the strftime method in Python's datetime module. The function should return the `datetime_str` converted to the format specified by `format_str`.
"""

import datetime

def convert_datetime_format(datetime_str, format_str):
    """
    Converts a given datetime string to a specified format.

    Args:
        datetime_str (str): The datetime string in the format "dd/mm/yyyy hh:mm:ss".
        format_str (str): A valid format string for the strftime method.

    Returns:
        str: The datetime_str converted to the format specified by format_str.
    """
    # Convert the given DateTime string to a datetime object
    given_datetime_obj = datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M:%S")
    
    # Convert the datetime object to the specified format
    formatted_datetime_str = given_datetime_obj.strftime(format_str)
    
    return formatted_datetime_str