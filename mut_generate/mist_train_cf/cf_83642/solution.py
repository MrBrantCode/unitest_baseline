"""
QUESTION:
Create a function called `validate_phone_number` that takes a string as input and returns a boolean value. The function should use a regular expression pattern to validate the input string against the standard United States telephone number formats, including 123-456-7890, (123) 456-7890, 123 456 7890, 123.456.7890, and +1 123 456 7890. The function should return True if the input string matches the pattern and False otherwise.
"""

import re

def validate_phone_number(number):
    pattern = re.compile((
        "^" # Start of string
        "(\\+1\\s)?" # Optional "+1" at the start
        "(\\()?\\d{3}(?(2)\\))" # First 3 digits potentially bracketed
        "[\\.\\s-]?" # Optional separator
        "\\d{3}" # Next 3 digits
        "[\\.\\s-]?" # Optional separator
        "\\d{4}" # Last 4 digits
        "$" # End of string
    ))
    
    return bool(pattern.match(number))