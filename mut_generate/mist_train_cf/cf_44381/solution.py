"""
QUESTION:
Create a function `compile_pattern` that compiles a regular expression pattern using Python's `re` module. The pattern should match numerical values containing exactly three decimal places, optionally allowing or excluding values with no digits before the decimal point.
"""

import re
def compile_pattern(optional_digits=True):
    """
    Compiles a regular expression pattern to match numerical values containing 
    exactly three decimal places, optionally allowing or excluding values with 
    no digits before the decimal point.

    Args:
        optional_digits (bool): If True, allows values with no digits before 
            the decimal point. If False, requires at least one digit before 
            the decimal point. Defaults to True.

    Returns:
        re.Pattern: A compiled regular expression pattern.
    """
    if optional_digits:
        return re.compile(r'^\d*\.\d{3}$')
    else:
        return re.compile(r'^\d+\.\d{3}$')