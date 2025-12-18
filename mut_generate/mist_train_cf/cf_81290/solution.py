"""
QUESTION:
Create a function `validate_date(date_string)` that takes a date string as input in the format MM/DD/YYYY and returns `True` if the date string is valid and `False` otherwise. A valid date string must match the MM/DD/YYYY format and represent a legitimate date, including correct day and month values and leap year conditions.
"""

import re
from datetime import datetime

def validate_date(date_string):
    # Check against regular expression
    date_pattern = re.compile(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/([12][0-9]{3})$')
    if not date_pattern.match(date_string):
        return False

    # Check if it's an actual date
    try:
        datetime.strptime(date_string, '%m/%d/%Y')
        return True
    except ValueError:
        return False