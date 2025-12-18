"""
QUESTION:
Construct a function named `replace_chars` that takes an input string and a list of characters to replace as arguments. This function should replace each occurrence of the specified characters in the input string with a semicolon (`;`) while preserving the original case of alphabets. The function should handle edge cases where the input string is null or empty and should be able to process large inputs efficiently.
"""

import re

def replace_chars(input_string, chars_to_replace):
    if not input_string:  
        return input_string

    chars_to_replace = set(chars_to_replace)  
    output_string = ''

    for char in input_string:
        if char in chars_to_replace:
            if char == ';':  
                output_string += char
            else:
                output_string += ';'
        else:
            output_string += char

    return output_string