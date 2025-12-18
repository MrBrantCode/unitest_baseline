"""
QUESTION:
Create a function `process_strings` that takes a list of strings as input and returns a new list of strings. The function should exclude any strings that contain numbers or special characters. Additionally, it should exclude any strings whose reverse is also present in the original list. If the input is not a list or if any element in the list is not a string, the function should return an error message and `None`.
"""

import re

def process_strings(list_of_strings):
    if not isinstance(list_of_strings, list):
        return "Error: Input is not a list."
    for word in list_of_strings:
        if not isinstance(word, str):
            return "Error: List contains non-string elements."
    output = []
    for word in list_of_strings:
        if re.search('^[a-zA-Z]*$', word) and word[::-1] not in list_of_strings:
            output.append(word)
    return output