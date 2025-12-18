"""
QUESTION:
Create a function named `is_alphabetic` that takes a string `s` as input and returns a boolean value indicating whether the string exclusively consists of alphabetic characters (both lowercase and uppercase) and/or hyphenated words. The function should consider a word as a sequence of characters that begins and ends with a letter and may contain hyphens.
"""

import re

def is_alphabetic(s):
    pattern = r'^[A-Za-z]+(-[A-Za-z]+)*$'
    return re.match(pattern, s) is not None