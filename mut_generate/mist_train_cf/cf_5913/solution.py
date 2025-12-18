"""
QUESTION:
Write a function `check_reverse_substring` that checks if a string contains a given substring in reverse order. The function should be case-insensitive and ignore punctuation marks and special characters. It takes two parameters: `string` and `substring`, and returns `True` if the reversed substring is found in the string, `False` otherwise.
"""

import re

def check_reverse_substring(string, substring):
    string = string.lower()
    substring = substring.lower()

    string = re.sub('[^a-zA-Z0-9]', '', string)
    substring = re.sub('[^a-zA-Z0-9]', '', substring)

    substring_reversed = substring[::-1]
    string_reversed = string[::-1]

    return substring_reversed in string_reversed