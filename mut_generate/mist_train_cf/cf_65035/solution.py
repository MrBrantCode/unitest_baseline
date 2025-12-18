"""
QUESTION:
Write a function `invert_case(s)` that takes a string `s` as input, inverts the case of its alphabetic characters (leaving non-alphabetic characters unchanged), and returns the result. The function should also check if the length of `s` is no more than 100 characters, and if not, return an error message instead.
"""

def invert_case(s):
    if len(s) > 100:
        return "Error: String length must not exceed 100 characters"
    else:
        return s.swapcase()