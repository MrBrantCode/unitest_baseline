"""
QUESTION:
Write a function named `verify_string` that takes a string `s` as input. The function should verify if `s` starts with a special character from the set ['@', '#', '$'], followed by exactly 3 lowercase and/or uppercase letters, contains at least one symbolic character from the set ['%', '^', '&'] in its middle part, and ends with 3 to 6 hexadecimal digits.
"""

import re

def verify_string(s):
    pattern = r'^[@#$][a-zA-Z]{3}.*[%^&].*[0-9A-Fa-f]{3,6}$'
    return bool(re.fullmatch(pattern, s))