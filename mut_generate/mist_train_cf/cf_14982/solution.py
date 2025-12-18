"""
QUESTION:
Create a regex expression for a function `date_validator` that matches and validates dates in the format dd/mm/yyyy, dd-mm-yyyy, or dd.mm.yyyy. The expression should ensure the day is between 1-31, the month is between 1-12, and the year is valid considering leap years.
"""

import re
from datetime import datetime

def date_validator(date_str):
    pattern = r"^(0[1-9]|[12][0-9]|3[01])([\/.-])(0[1-9]|1[0-2])\2\d{4}$"
    match = re.match(pattern, date_str)
    
    if match:
        day, month, year = map(int, match.group(0).replace('/', '-').split('-'))
        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False
    return False