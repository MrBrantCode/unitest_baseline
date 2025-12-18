"""
QUESTION:
Write a function `capitalize_and_remove_special` that takes a list of strings as input and returns a new list. The function should capitalize all strings in the input list and exclude any strings containing special characters (non-alphanumeric and non-whitespace). The function must have a time complexity of O(n), where n is the total number of characters in all the input strings.
"""

import re

def capitalize_and_remove_special(strings):
    result = []
    for string in strings:
        # Check if the string contains special characters
        if not re.match("^[a-zA-Z0-9\s]*$", string):
            continue

        # Capitalize the string and add it to the result list
        result.append(string.upper())

    return result