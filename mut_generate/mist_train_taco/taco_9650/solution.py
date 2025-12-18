"""
QUESTION:
Create a function that will return ```true``` if the input is in the following date time format ```01-09-2016 01:20``` and ```false``` if it is not.

This Kata has been inspired by the Regular Expressions chapter from the book Eloquent JavaScript.
"""

from re import match

def is_valid_datetime(date_time_str: str) -> bool:
    """
    Checks if the input string is in the datetime format '01-09-2016 01:20'.

    Parameters:
    date_time_str (str): The input string to be checked.

    Returns:
    bool: True if the input string matches the datetime format, otherwise False.
    """
    return bool(match(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}', date_time_str))