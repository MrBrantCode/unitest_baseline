"""
QUESTION:
Implement a function `replace_from_index` that replaces all occurrences of a given pattern in a string, starting from a specified index, while excluding certain characters from being replaced. The function should take five parameters: `input_str` (the input string), `pattern` (the regular expression pattern), `replacement` (the replacement string), `index` (the starting index), and `exclude_chars` (a list of characters that should be excluded from replacement). The function should return the modified input string.
"""

import re

def replace_from_index(input_str, pattern, replacement, index, exclude_chars):
    matches = re.finditer(pattern, input_str[index:])
    
    for match in matches:
        start = match.start() + index
        end = match.end() + index
        excluded = any(char in input_str[start:end] for char in exclude_chars)

        if not excluded:
            input_str = input_str[:start] + replacement + input_str[end:]

    return input_str