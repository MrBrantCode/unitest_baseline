"""
QUESTION:
Create a function named `validate_date` that takes a string as input and returns a boolean indicating whether the string is a valid date in the format MM/DD/YYYY. The function should account for leap years and the varying number of days in each month. The input string may contain invalid dates that cannot be parsed into a valid date, such as February 30.
"""

import re
from datetime import datetime

def validate_date(date_string):
    pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|1\d|2\d|3[01])/(\d{4})$"

    if not re.fullmatch(pattern, date_string):
        return False

    try:
        # This will raise a ValueError for invalid dates
        datetime.strptime(date_string, '%m/%d/%Y')
        return True
    except ValueError:
        return False