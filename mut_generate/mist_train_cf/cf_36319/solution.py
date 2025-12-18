"""
QUESTION:
Create a function named `parse_date_to_epoch` that takes a string `date_str` as input and returns the epoch timestamp as an integer, or `None` if parsing fails. The `date_str` can be in either of two formats: "%a %b %d %H:%M:%S %Y" or "%a %b %d %H:%M:%S %Z %Y", and the function should attempt to parse the string in this order.
"""

import time
import calendar
from typing import Union

def parse_date_to_epoch(date_str: str) -> Union[int, None]:
    for format_string in ["%a %b %d %H:%M:%S %Y", "%a %b %d %H:%M:%S %Z %Y"]:
        try:
            epoch = calendar.timegm(time.strptime(date_str, format_string))
            return epoch
        except ValueError:
            pass
    return None