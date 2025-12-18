"""
QUESTION:
Write a function called `convert_datetime_format` that takes two parameters: `given_datetime_str` and `format_str`. The function should convert the given `given_datetime_str` to the specified `format_str` using the Python datetime module. The `given_datetime_str` should be in the format "dd/mm/yyyy hh:mm:ss" and the `format_str` should be a valid format string for the strftime method. The function should return the converted datetime string.
"""

import datetime

def convert_datetime_format(given_datetime_str, format_str):
    given_datetime_obj = datetime.datetime.strptime(given_datetime_str, "%d/%m/%Y %H:%M:%S")
    return given_datetime_obj.strftime(format_str)