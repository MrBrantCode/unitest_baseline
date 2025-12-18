"""
QUESTION:
Create a function `remove_consecutive_whitespaces(string)` that takes a string as input, replaces all consecutive whitespaces with a single space, ignores any whitespaces at the beginning or end of the string, and handles cases where the input string contains non-alphanumeric characters. The function should have a time complexity of O(n), where n is the length of the input string.
"""

import re

def remove_consecutive_whitespaces(string):
    cleaned_string = re.sub(r'\s+', ' ', string.strip())
    return cleaned_string