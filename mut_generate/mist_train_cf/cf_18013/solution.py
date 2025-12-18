"""
QUESTION:
Create a function `is_string_contained(str_1, str_2)` that determines whether `str_1` is a substring of `str_2`, ignoring case and leading/trailing whitespace. The function should return a boolean and have a time complexity of O(n), where n is the length of the longer string.
"""

def is_string_contained(str_1, str_2):
    str_1 = str_1.strip().lower()
    str_2 = str_2.strip().lower()
    return str_1 in str_2