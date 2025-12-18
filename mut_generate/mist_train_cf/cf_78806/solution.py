"""
QUESTION:
Create a function `match_pattern` that takes a string as an input and returns a boolean value indicating whether the string matches the following conditions: 
- starts with the characters "abc", 
- ends with the characters "xyz", and 
- contains at least two occurrences of digits between "abc" and "xyz".
"""

import re

def match_pattern(string):
    pattern = re.compile(r'abc(?=.*[0-9].*?[0-9].*).*xyz$')
    return bool(pattern.match(string))