"""
QUESTION:
Write a function `process_string(s)` that takes a string `s` as input and returns a tuple containing the modified string and a tuple of two counts. The function should replace all blank spaces in `s` with underscores and remove all special characters except for punctuation marks (.,!?'). The returned counts should represent the number of replacements (spaces changed to underscores) and removals (special characters dropped).
"""

import re

def process_string(s):
    replacements, removals = 0, 0
    new_s = ''

    for ch in s:
        if ch.isspace():
            new_s += '_'
            replacements += 1
        elif ch in ".,!?'" or ch.isalnum():
            new_s += ch
        else:
            removals += 1

    return (new_s, (replacements, removals))