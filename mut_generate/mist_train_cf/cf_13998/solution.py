"""
QUESTION:
Create a function `match_float` that takes a string as input and returns a boolean indicating whether the string matches a float number with at least one decimal place. The float number should be in the following format:
- It can be positive or negative.
- It can have an optional leading plus or minus sign.
- It can have an optional integer part before the decimal point.
- It must have at least one digit after the decimal point.
- The decimal point can be followed by zero or more digits.
- It can have an optional exponent part following the digits, represented using the letter 'e' or 'E' followed by an optional plus or minus sign and one or more digits.
"""

import re

def match_float(s):
    """
    This function checks if the input string matches a float number with at least one decimal place.
    
    Args:
        s (str): The input string to be checked.
    
    Returns:
        bool: True if the string matches a float number with at least one decimal place, False otherwise.
    """
    pattern = r'^[-+]?([0-9]*\.[0-9]+|[0-9]+\.[0-9]*)([eE][-+]?[0-9]+)?$'
    return bool(re.fullmatch(pattern, s))