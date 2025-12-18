"""
QUESTION:
Create a function `format_date_time(format_specifier, date_time_str)` that takes a format specifier and a date/time string as input. The function should parse the date/time string using the format `%a %b %d %H:%M:%S %Y` and then format it based on the given format specifier. 

The function should support two format specifiers: `%c` for the local version of date and time (e.g., "Mon Dec 31 17:41:00 2018") and `%x` for the local version of date (e.g., "12/31/18"). If the format specifier is neither `%c` nor `%x`, the function should return "Invalid format specifier".
"""

import datetime

def format_date_time(format_specifier, date_time_str):
    """
    This function formats a given date/time string based on a specified format.
    
    Parameters:
    format_specifier (str): The format specifier. It can be either '%c' for the local version of date and time or '%x' for the local version of date.
    date_time_str (str): The date/time string to be formatted. It should be in the format '%a %b %d %H:%M:%S %Y'.
    
    Returns:
    str: The formatted date/time string if the format specifier is valid, 'Invalid format specifier' otherwise.
    """

    date_time = datetime.datetime.strptime(date_time_str, "%a %b %d %H:%M:%S %Y")
    
    if format_specifier == '%c':
        formatted_date_time = date_time.strftime("%a %b %d %H:%M:%S %Y")
    elif format_specifier == '%x':
        formatted_date_time = date_time.strftime("%m/%d/%y")
    else:
        formatted_date_time = "Invalid format specifier"
    
    return formatted_date_time