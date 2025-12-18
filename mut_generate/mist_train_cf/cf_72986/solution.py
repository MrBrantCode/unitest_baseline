"""
QUESTION:
Create a function called `validate_date` that takes a string as an argument and returns `True` if the string represents a valid date in the MM/DD/YYYY format and `False` otherwise. The function should validate the month (01-12), day (01-31), and year (0000-9999) segments, but it does not need to check for the correctness of the date, such as the number of days in each month or leap years.
"""

import re

def validate_date(date_string):
    pattern = r"(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}"
    if re.fullmatch(pattern, date_string):
        return True
    else:
        return False