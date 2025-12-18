"""
QUESTION:
Create a function `validate_date` that takes a string representing a date in the format "yyyy-mm-dd" as input and returns a boolean indicating whether the date is valid. The date is valid if it is between the years 1900 to 2099, has a valid month (01-12), and has a valid day (01-31) for that month. Note that this function should not consider the actual number of days in each month, i.e., it will consider dates like "2000-02-30" as valid.
"""

import re

def validate_date(date):
    regex = "^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$"
    match = re.match(regex, date)
    return match is not None