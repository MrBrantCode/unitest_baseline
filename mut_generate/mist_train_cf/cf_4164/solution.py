"""
QUESTION:
Create a function named `convert_to_camel_case` that takes a string as input. The function should convert the string to CamelCase if it contains at least one uppercase letter, one digit, and one special character. If the string does not meet these conditions, it should return the original string. The function should handle strings with multiple words separated by underscores or hyphens, as well as strings that start or end with underscores or hyphens.
"""

import re

def convert_to_camel_case(string):
    if not (any(char.isupper() for char in string) and
            any(char.isdigit() for char in string) and
            re.search('[^a-zA-Z0-9]', string)):
        return string

    string = re.sub('[_-]', ' ', string)
    string = ''.join(word.capitalize() for word in string.split())

    return re.sub('[^a-zA-Z0-9]', '', string)