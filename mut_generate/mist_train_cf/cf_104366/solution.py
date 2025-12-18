"""
QUESTION:
Write a function `is_substring(string1, string2)` that checks if `string2` is a substring of `string1` in a case-insensitive manner, ignoring leading and trailing spaces in both strings. The function should return `True` if `string2` is a substring of `string1` and `False` otherwise.
"""

def is_substring(string1, string2):
    # Remove leading and trailing spaces
    string1 = string1.strip()
    string2 = string2.strip()

    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Check if string2 is a substring of string1
    return string2 in string1