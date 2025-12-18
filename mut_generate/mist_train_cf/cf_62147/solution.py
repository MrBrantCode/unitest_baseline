"""
QUESTION:
Create a function named `unique_chars` that takes two strings `s1` and `s2` as input. The function should remove all white spaces from `s1` and `s2`, concatenate the resulting strings, and return the number of unique characters in the concatenated string.
"""

def unique_chars(s1, s2):
    s3 = s1.replace(' ', '') + s2.replace(' ', '')
    return len(set(s3))