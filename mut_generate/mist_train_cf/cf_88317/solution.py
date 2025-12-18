"""
QUESTION:
Write a function `get_first_two_chars` that takes a string as input and returns the first two characters of the string. The function should not use any built-in string manipulation functions or methods, and its time complexity should be O(n), where n is the length of the string. The function should handle strings of any length.
"""

def get_first_two_chars(s):
    if len(s) < 2:
        return s
    first_two = s[0] + s[1]
    return first_two