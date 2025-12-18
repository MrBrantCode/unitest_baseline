"""
QUESTION:
Write a function called `reverse_string(s)` that takes a string `s` as input and returns the string with its characters in reverse order. The function should efficiently handle strings of any length and correctly handle edge cases where the input string is `None` or empty.
"""

def reverse_string(s):
    # Edge cases: Return s directly if it is None or empty
    if s is None or len(s) == 0:
        return s
    
    # Use Python's slicing feature
    return s[::-1]