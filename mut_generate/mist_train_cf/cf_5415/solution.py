"""
QUESTION:
Create a function `match_strings(string1, string2)` that checks if two input strings meet specific criteria. The function should return `True` if `string1` contains only a combination of lowercase and uppercase letters, `string2` contains a combination of lowercase letters, uppercase letters, digits, and special characters, and `string2` is a palindrome containing at least one digit; otherwise, return `False`.
"""

import re

def match_strings(string1, string2):
    pattern1 = r'^[a-zA-Z]+$'
    pattern2 = r'^(?=.*\d)[a-zA-Z0-9!@#$%^&*()-=_+]+$'
    
    if re.match(pattern1, string1) and re.match(pattern2, string2):
        if string2 == string2[::-1]:
            return True
    return False