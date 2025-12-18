"""
QUESTION:
Create a Python function `string_to_tuple(s)` that takes a string `s` representing a tuple of integers (e.g., "(1,2,3)") and returns the actual tuple of integers. The function should be able to handle strings with any number of comma-separated integers enclosed in parentheses.
"""

def string_to_tuple(s):
    return tuple(map(int, s[1:-1].split(',')))