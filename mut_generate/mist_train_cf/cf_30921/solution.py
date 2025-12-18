"""
QUESTION:
Write a function `processStrings(strings)` that takes a list of strings and returns a modified list. The function should process each string in the list according to the following rules:
- If a string contains "should" followed by "be", remove everything between "should" and "be" (inclusive).
- If a string contains "always" followed by "drop", remove everything between "always" and "drop" (inclusive).
"""

import re

def entrance(strings):
    modified_strings = []
    for string in strings:
        modified_string = re.sub(r'should.*?be', 'be', string)
        modified_string = re.sub(r'always.*?drop', 'drop', modified_string)
        modified_strings.append(modified_string)
    return modified_strings