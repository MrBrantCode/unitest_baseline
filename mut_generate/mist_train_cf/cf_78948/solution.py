"""
QUESTION:
Write a function `parse_string_to_dict(s)` that takes a string of comma-separated key-value pairs as input, where each key-value pair is separated by an equal sign (=) and there may be whitespace around the equal sign. The function should return a dictionary where the characters before "=" represent the keys and the characters after "=" represent the values, handling both integers and floating point numbers as values.
"""

import re

def parse_string_to_dict(s):
    key_value_pairs = s.split(',')
    result_dict = {}

    for pair in key_value_pairs:
        match = re.match(r'\s*(\w+)\s*=\s*([\d\.]+)\s*', pair)
        if match:
            result_dict[match.group(1)] = float(match.group(2)) if '.' in match.group(2) else int(match.group(2))
            
    return result_dict