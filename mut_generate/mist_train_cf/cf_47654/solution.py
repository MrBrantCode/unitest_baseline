"""
QUESTION:
Create a function `last_non_space_char(string)` that returns the last non-space character in a given string. The function should remove any trailing spaces and ensure the string has at least one non-space character. If no non-space character is found, return an error message.
"""

def last_non_space_char(string):
    string = string.rstrip()
    if len(string) > 0:
        return string[-1]
    else:
        return 'Error: No non-space character found'