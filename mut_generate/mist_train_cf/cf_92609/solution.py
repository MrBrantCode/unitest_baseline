"""
QUESTION:
Create a function named `join_with_reverse` that takes two strings as input, `string1` and `string2`, and returns a single string with the second string reversed and placed in the middle of the first string.
"""

def join_with_reverse(string1, string2):
    return string1 + string2[::-1] + string1