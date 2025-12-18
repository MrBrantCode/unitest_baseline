"""
QUESTION:
Create a function `check_string` that takes a string as input and returns `True` if the string meets the following conditions: 
- The string contains only uppercase letters, lowercase letters, numbers, or special characters from the set "@#$%^&+=".
- The string has a length of at most 100 characters.
- The string contains at least one uppercase letter, one lowercase letter, one number, and one special character from the set "@#$%^&+=".
The function should return `False` otherwise.
"""

import re

def check_string(string):
    # Check if all characters are either uppercase letters, lowercase letters, numbers, or special characters
    if re.match("^[A-Za-z0-9@#$%^&+=]{1,100}$", string):
        # Check if the string contains at least one uppercase letter, one lowercase letter, one number, and one special character
        if any(char.isupper() for char in string) and any(char.islower() for char in string) and any(char.isdigit() for char in string) and any(char in "@#$%^&+=" for char in string):
            return True
    return False