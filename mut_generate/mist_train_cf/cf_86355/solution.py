"""
QUESTION:
Create a function called `modify_string` that takes a string as input, removes all whitespace, punctuation, and digits, converts the resulting string to uppercase, and returns the string with its characters sorted in descending order.
"""

import string

def modify_string(s):
    # Remove whitespace, punctuation, and digits
    s = ''.join([char for char in s if char not in string.whitespace and char not in string.punctuation and not char.isdigit()])
    
    # Convert to uppercase
    s = s.upper()
    
    # Sort in descending order
    return ''.join(sorted(s, reverse=True))