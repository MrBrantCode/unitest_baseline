"""
QUESTION:
Create a function `check_string_contains` that takes two parameters `str_1` and `str_2` and returns a boolean indicating whether `str_1` is contained in `str_2`. The function should ignore any leading or trailing whitespace in both strings and be case-insensitive.
"""

def check_string_contains(str_1, str_2):
    str_1 = str_1.strip().lower()
    str_2 = str_2.strip().lower()
    return str_1 in str_2