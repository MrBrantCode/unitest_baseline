"""
QUESTION:
Create a function named `split_string` that takes a string and a separator as input, splits the string into substrings based on the separator, and returns the substrings in a list. The separator can be any combination of characters and can occur multiple times within the string. The function should handle cases where the separator occurs at the beginning or end of the string, and consecutive separators should not result in empty substrings in the output. The function should only split the string if the separator is surrounded by letters or numbers, and ignore any separator within a substring enclosed in double quotes.
"""

import re

def split_string(string, separator):
    regex = r'"[^"]*"|[^' + re.escape(separator) + ']+'
    substrings = re.findall(regex, string)
    substrings = [substring.strip() for substring in substrings]
    return substrings