"""
QUESTION:
Write a function `validate_zip` to validate a 5-digit numeric zip code using a regular expression. The function should handle any exceptions that may be raised by the regular expression. The input to the function will be a string representing the zip code. The function should return a string indicating whether the zip code is valid or not.
"""

import re

def validate_zip(zip_code):
    try:
        pattern = re.compile(r'^\d{5}$') 
        if pattern.match(zip_code):
            return "Zip Code is VALID."
        else:
            return "Zip Code is INVALID."
    except re.error as err:
        return f"Error: {err}"