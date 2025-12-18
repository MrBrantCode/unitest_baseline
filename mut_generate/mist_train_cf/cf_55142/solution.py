"""
QUESTION:
Write a function `normalize_string` that takes a string as input and returns a normalized string. The normalization process involves converting the string to lowercase, replacing all blank spaces with an empty string, and transforming non-alphanumeric characters into underscore symbols. The function should handle potential Unicode and escape characters. The output string should not contain leading or trailing underscores, and sequential underscores should be replaced with a single underscore.
"""

import re

def normalize_string(input_string):
    input_string = input_string.lower()
    input_string = re.sub(r'\W', '_', input_string)
    input_string = re.sub(r'_+', '_', input_string)
    input_string = re.sub(r'^_|_$', '', input_string)
    return input_string