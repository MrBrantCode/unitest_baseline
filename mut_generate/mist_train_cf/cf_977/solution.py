"""
QUESTION:
Create a function called `capitalize_and_remove_special` that takes a list of strings as input. The function should return a new list containing the capitalized version of each string that only consists of alphanumeric characters and whitespace, and exclude strings with any special characters. The function should have a time complexity of O(n), where n is the total number of characters in all the input strings.
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