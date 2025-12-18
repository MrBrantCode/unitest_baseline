"""
QUESTION:
Create a function `match_CDE` that checks if a given string contains the characters "C", "D", and "E" in any order, with each character appearing exactly once. The function should be case-insensitive and should only match strings with a maximum length of 10 characters.
"""

import re

def match_CDE(string):
    if len(string) > 10:
        return False
    pattern = r'^(?=.*[cC])(?=.*[dD])(?=.*[eE])[cCdDeE]{3}$'
    match = re.match(pattern, string)
    return bool(match)