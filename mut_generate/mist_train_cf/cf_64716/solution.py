"""
QUESTION:
Write a function `exclude_alphanumerics` that takes an array of strings as input and returns a list of strings that consist only of non-alphanumeric characters. The function should use a regular expression to filter out the alphanumeric strings.
"""

import re

def exclude_alphanumerics(arr):
    pattern = r"^\W+$" # regex pattern to match non-alphanumeric characters
    result = [i for i in arr if re.match(pattern, i)]
    return result