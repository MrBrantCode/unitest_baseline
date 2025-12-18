"""
QUESTION:
Create a function `swap_chars` that takes a string as input and returns a new string with the first and last characters swapped. The function should leave strings of length 1 or less unchanged.
"""

def swap_chars(s):
    if len(s) > 1:
        return s[-1] + s[1:-1] + s[0]
    return s