"""
QUESTION:
Create a function `validate_string` that takes a string as input and returns `True` if the string meets the following conditions:
- The string starts with a letter.
- The string contains only letters and numbers.
- The string is at least 8 characters long.
- The string does not contain any repeated characters.
Implement this function using recursion.
"""

import re

def validate_string(string):
    # Base case: check if string is at least 8 characters long
    if len(string) < 8:
        return False
    
    # Check if string starts with a letter
    if not string[0].isalpha():
        return False
    
    # Check if string contains only letters and numbers
    if not re.match("^[a-zA-Z0-9]+$", string):
        return False
    
    # Check if string contains any repeated characters
    for i in range(len(string)):
        if string[i] in string[i+1:]:
            return False
    
    # Base case: if all conditions are satisfied, return True
    return True