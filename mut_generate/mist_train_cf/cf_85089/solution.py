"""
QUESTION:
Extract distinct terms between two signifiers in a string using regex.

Create a function `find_terms` that takes three parameters: `string`, `signifier1`, and `signifier2`. The function should extract all distinct terms between `signifier1` and `signifier2` in the given `string` and return them as a list. The function should handle cases where `signifier1` and `signifier2` have special meanings in regex by escaping them with a backslash.
"""

import re

def find_terms(string, signifier1, signifier2):
    pattern = '\\' + signifier1 + '(.*?)' + '\\' + signifier2
    match = re.findall(pattern, string)
    return list(set(match))  # using set to remove duplicates