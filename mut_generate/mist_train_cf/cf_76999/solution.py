"""
QUESTION:
Create a function `remove_duplicates_and_reverse` that takes a string as input and returns the string with duplicates removed and characters in reverse order. The original order of non-duplicated characters must be preserved. The input string can contain symbols, numbers, and whitespaces.
"""

def remove_duplicates_and_reverse(input_str):
    seen = set()
    output_str = ''
    for char in input_str:
        if char not in seen:
            output_str += char
            seen.add(char)
    return output_str[::-1]