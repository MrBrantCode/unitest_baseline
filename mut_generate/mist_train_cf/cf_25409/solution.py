"""
QUESTION:
Write a function called `collapse_repeating_chars` that takes a string as input and returns a new string where all sequences of repeating continuous characters are collapsed into a single character.
"""

def collapse_repeating_chars(s):
    result = ""
    for char in s:
        if not result or char != result[-1]:
            result += char
    return result