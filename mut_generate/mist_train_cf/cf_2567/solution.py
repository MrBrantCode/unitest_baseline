"""
QUESTION:
Create a function called `check_string` that takes a single string as input and returns `True` if the string meets the following conditions:

- It contains at least one uppercase letter.
- It contains at least one lowercase letter.
- It contains at least one special character (defined by the string module's `punctuation` attribute).
- It contains at least one digit.

The function should return `False` if any of these conditions are not met. The function should have a time complexity of O(n), where n is the length of the string.
"""

import string

def check_string(s):
    # check if string contains at least one uppercase and one lowercase letter
    if not any(char.isupper() for char in s) or not any(char.islower() for char in s):
        return False
    
    # check if string contains at least one special character
    if not any(char in string.punctuation for char in s):
        return False
    
    # check if string contains at least one digit
    if not any(char.isdigit() for char in s):
        return False
    
    return True