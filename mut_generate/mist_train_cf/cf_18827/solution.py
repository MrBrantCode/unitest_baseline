"""
QUESTION:
Develop a function named `get_first_two_chars` that takes a string `s` as input and returns the first two characters of the string. The function must have a time complexity of O(1) and cannot use any built-in string manipulation functions or methods. If the string has less than two characters, the function should return the string as is.
"""

def get_first_two_chars(s):
    if len(s) < 2:  # Check if the string has less than two characters
        return s  # Return the string as is
    return s[0] + s[1]  # Return the first two characters of the string