"""
QUESTION:
Write a function `extract_numeric_values` that takes a string as input and returns a list of numeric values. The string contains placeholders in the format of `%i` for integers, `%f` for floating point numbers, and `%x` for hexadecimal numbers. The function should handle nested placeholders and multiple occurrences of the same placeholder, and ignore any placeholders that are not followed by a valid numeric value.
"""

import re

def extract_numeric_values(format_string):
    pattern = r'%([ifx])(?:-(%[ifx]))*'
    matches = re.findall(pattern, format_string)
    numeric_values = []

    for match in matches:
        placeholder = match[0]
        subplaceholders = match[1:]

        for subplaceholder in subplaceholders:
            if subplaceholder:
                format_string = format_string.replace(subplaceholder, placeholder)

        sub_values = re.findall(r'\d+(?:\.\d+)?', format_string)
        numeric_values.extend(sub_values)

    return numeric_values