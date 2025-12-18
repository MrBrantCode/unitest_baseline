"""
QUESTION:
Implement a function `validate_and_convert_iso8601` that takes an input string representing a date in ISO 8601 format ('YYYY-MM-DD'), validates whether the input string conforms to this format, and if valid, converts it to the format 'dd-mm-yyyy'. The function should return a tuple containing a boolean indicating the validity of the input string and the converted date string if valid, or an error message if invalid.
"""

import datetime

def validate_and_convert_iso8601(date_string):
    try:
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return (True, date.strftime('%d-%m-%Y'))
    except ValueError:
        return (False, 'Invalid date format')