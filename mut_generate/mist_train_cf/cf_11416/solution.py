"""
QUESTION:
Write a function `filter_strings` that takes a list of strings as input and returns a list of strings that start with a letter and end with a number, and do not contain any special characters. The function should use a Python regex pattern to achieve this.
"""

import re

def filter_strings(string_list):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*[0-9]$'
    return [string for string in string_list if re.match(pattern, string)]