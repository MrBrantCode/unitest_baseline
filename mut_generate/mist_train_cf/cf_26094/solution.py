"""
QUESTION:
Write a function that takes a string as input and returns True if the string matches the phone number format (999) 999-9999, where 9 represents any digit. The function should return False otherwise.
"""

import re

def is_phone_number(s):
    """
    Returns True if the string matches the phone number format (999) 999-9999, 
    where 9 represents any digit. Otherwise, returns False.
    """
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    return bool(re.match(pattern, s))