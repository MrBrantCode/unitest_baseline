"""
QUESTION:
Write a regex to validate a 24 hours time string.
See examples to figure out what you should check for:

Accepted:
01:00 - 1:00  

Not accepted:

24:00

You should check for correct length and no spaces.
"""

import re

def is_valid_24_hour_time(time_str: str) -> bool:
    """
    Validates whether the given string is a valid 24-hour time format.

    Args:
        time_str (str): The time string to be validated.

    Returns:
        bool: True if the time string is valid, False otherwise.
    """
    _24H = re.compile('^([01]?\\d|2[0-3]):[0-5]\\d$')
    return bool(_24H.match(time_str))