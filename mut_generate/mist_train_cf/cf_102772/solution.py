"""
QUESTION:
Implement a function `combine_strings(str1, str2)` that takes two input strings and returns a new string that is the result of concatenating `str1` and `str2` without using any built-in string concatenation functions or operators.
"""

def combine_strings(str1, str2):
    combined = ""
    for char in str1:
        combined += char
    for char in str2:
        combined += char
    return combined