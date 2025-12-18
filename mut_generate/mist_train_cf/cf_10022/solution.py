"""
QUESTION:
Create a regular expression pattern to match strings composed of lowercase letters "a" through "e" with the following conditions: the string must only contain these letters and not any other characters, and it must not contain any consecutive duplicate letters. The pattern should match strings from start to end.
"""

import re

def no_consecutive_duplicates(s):
    pattern = r'^(?!.*(.)\1)[a-e]+$'
    return bool(re.match(pattern, s))