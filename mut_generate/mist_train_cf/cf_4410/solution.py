"""
QUESTION:
Write a function `clean_and_sort_string` that takes a string as input, removes all non-alphanumeric characters using regular expression, converts the resulting string to lowercase, and returns the string sorted in reverse alphabetical order.
"""

import re

def clean_and_sort_string(input_string):
    clean_string = re.sub(r'[^a-zA-Z0-9]', '', input_string.lower())
    return ''.join(sorted(clean_string, reverse=True))