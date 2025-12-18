"""
QUESTION:
Implement a recursive function `switch_chars(s)` that takes a string `s` as input and switches the first and last characters until they all meet at the center of the string. The function should retain the integrity of the string, not introduce new characters, and not interfere with the sequence of other characters, including special characters or symbols. The function should be optimized in terms of space and time complexity.
"""

def switch_chars(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + switch_chars(s[1:-1]) + s[0]