"""
QUESTION:
Create a function named `match_strings` that takes two strings as input, `string1` and `string2`, and returns `True` if the strings match the following criteria and `False` otherwise. The criteria are:
- `string1` must contain only a combination of lowercase and uppercase letters.
- `string2` must contain a combination of lowercase letters, uppercase letters, digits, and special characters.
- `string2` must be a palindrome.
- `string2` must contain at least one digit.
"""

import re

def match_strings(string1, string2):
    pattern1 = r'^[a-zA-Z]+$'
    pattern2 = r'^(?=.*\d)[a-zA-Z0-9!@#$%^&*()-=_+]+$'
    
    if re.match(pattern1, string1) and re.match(pattern2, string2):
        if string2 == string2[::-1]:
            return True
    return False