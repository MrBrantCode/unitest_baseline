"""
QUESTION:
Create a function named `match_pattern` that takes a string as input and returns a boolean indicating whether the string matches the following pattern: 
The string starts with one or more '1's, followed by one or more hexadecimal characters, then a lowercase English alphabet vowel, and finally ends with zero or more '0's followed by zero or more '1's.
"""

import re

def match_pattern(string):
    pattern = r'^1+[0-9A-Fa-f]+[aeiou]0*1*$'
    match = re.match(pattern, string)
    return match is not None