"""
QUESTION:
Construct a password regex pattern based on boolean conditions. 

Create a function named `construct_password_regex` that takes four parameters: `min_length`, `max_length`, and three boolean flags `requires_small_letter`, `requires_capital_letter`, `requires_special_char`. The function should return a regex pattern that matches any string of length between `min_length` and `max_length` (inclusive) containing at least one small letter if `requires_small_letter` is True, one capital letter if `requires_capital_letter` is True, and one special character (any of `@$!%*?&`) if `requires_special_char` is True. The regex pattern should also allow alphanumeric characters and special characters (any of `@$!%*?&`) if `requires_special_char` is True.

The function should be able to handle the case when all the boolean flags are False, in which case the regex pattern should match any alphanumeric string of the specified length.
"""

import re

def construct_password_regex(min_length, max_length, requires_small_letter, requires_capital_letter, requires_special_char):
    """
    Construct a password regex pattern based on boolean conditions.

    Args:
        min_length (int): The minimum length of the password.
        max_length (int): The maximum length of the password.
        requires_small_letter (bool): Whether the password requires a small letter.
        requires_capital_letter (bool): Whether the password requires a capital letter.
        requires_special_char (bool): Whether the password requires a special character.

    Returns:
        str: A regex pattern that matches the password conditions.
    """
    regex_str = '^'
    
    if requires_small_letter:
        regex_str += '(?=.*[a-z])'
    
    if requires_capital_letter:
        regex_str += '(?=.*[A-Z])'
    
    if requires_special_char:
        regex_str += '(?=.*[@$!%*?&])'
    
    regex_str += '[A-Za-z'
    
    if requires_special_char:
        regex_str += '@$!%*?&'
    
    regex_str += ']{' + str(min_length) + ',' + str(max_length) + '}$'
    
    return regex_str