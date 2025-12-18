"""
QUESTION:
Create a function `remove_consecutive_whitespaces` that takes a string as input, replaces all consecutive whitespaces with a single space, and removes any leading or trailing whitespaces. The function should handle non-alphanumeric characters correctly and have a time complexity of O(n), where n is the length of the input string.
"""

import re

def remove_consecutive_whitespaces(string):
    cleaned_string = re.sub(r'\s+', ' ', string.strip())
    return cleaned_string