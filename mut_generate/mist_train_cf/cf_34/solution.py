"""
QUESTION:
Write a function named `reverse_string` that takes an input string `user_string` and returns the reversed string of alphabetic characters. The function must be case-insensitive and the input string must meet the following conditions: 
- it must contain at least one alphabetic character, 
- it cannot be longer than 100 characters, 
- special characters must be removed, and 
- the function should only reverse the alphabetic characters.
"""

import re

def reverse_string(user_string):
    if len(user_string) == 0 or len(user_string) > 100 or not any(c.isalpha() for c in user_string):
        return ""
    else:
        user_string = re.sub(r'[^a-zA-Z]', '', user_string)
        reversed_string = ""
        for char in user_string:
            reversed_string = char.upper() + reversed_string
        return reversed_string