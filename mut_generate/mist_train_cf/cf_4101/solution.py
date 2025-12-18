"""
QUESTION:
Create a function `get_first_two_chars` that takes a string `s` as input and returns the first two characters of the string. The function must have a time complexity of O(n), where n is the length of the string, and cannot use any built-in string manipulation functions or methods. If the string has a length of less than 2, the function should return the entire string.
"""

def get_first_two_chars(s):
    if len(s) < 2:
        return s
    first_two = s[0] + s[1]
    return first_two