"""
QUESTION:
Create a function `determine_data_type(value)` that determines the data type of a given value. The function should use regular expressions to determine the data type and have a time complexity of O(n), where n is the length of the value.
"""

import re

def determine_data_type(value):
    pattern = r'^".*"$'  # Regular expression pattern for a string
    if re.match(pattern, value):
        return "string"
    else:
        return "unknown"