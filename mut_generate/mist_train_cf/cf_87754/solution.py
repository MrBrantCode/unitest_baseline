"""
QUESTION:
Write a function `is_substring` that checks if a given string (`string2`) is a substring of another string (`string1`), ignoring case and leading/trailing spaces. The function should return `False` if either `string1` or `string2` is empty or contains only spaces.
"""

def is_substring(s1, s2):
    # Remove leading and trailing spaces
    s1 = s1.strip()
    s2 = s2.strip()

    # Check if input strings are empty or contain only spaces
    if len(s1) == 0 or len(s2) == 0:
        return False

    # Convert both strings to lowercase for case-insensitive comparison
    s1 = s1.lower()
    s2 = s2.lower()

    # Check if string2 is a substring of string1
    return s2 in s1