"""
QUESTION:
Write a function `change_date_format` that takes a string of dates in the format 'dd/mm/yyyy' and returns the string with the dates converted to 'mm/dd/yyyy'. The function should also validate each date according to the Gregorian calendar and append ' is not a valid date!' to any invalid dates. Assume the input string is a comma-separated list of dates. Do not use any date-time libraries.
"""

import re

def change_date_format(dt):
    """
    This function takes a string of dates in the format 'dd/mm/yyyy' and returns the string 
    with the dates converted to 'mm/dd/yyyy'. The function also validates each date according 
    to the Gregorian calendar and appends ' is not a valid date!' to any invalid dates.

    Args:
        dt (str): A comma-separated list of dates in the format 'dd/mm/yyyy'.

    Returns:
        str: A comma-separated list of dates in the format 'mm/dd/yyyy' with invalid dates marked.
    """

    p = re.compile('(\d{2})/(\d{2})/(\d{4})')

    def validate_date(m):
        """Validate a date according to the Gregorian calendar."""
        day, month, year = map(int, m.groups())
        is_valid = (1 <= day <= 31) and (1 <= month <= 12)
        if is_valid:
            if month in (4, 6, 9, 11) and day > 30:
                is_valid = False
            elif month == 2:
                if ((year%4==0 and year%100!=0) or (year%400==0)) and day > 29:
                    is_valid = False
                elif day > 28:
                    is_valid = False
        return is_valid

    def swap(m):
        """Swap the date format and mark invalid dates."""
        if validate_date(m):
            return m.group(2) + '/' + m.group(1) + '/' + m.group(3)
        else:
            return m.group(0) + ' is not a valid date!'
            
    return p.sub(swap, dt)