"""
QUESTION:
Write a function `special_to_underscore` that takes a string as input and returns a new string where every special character in the input string is replaced with an underscore. The function should handle all possible special characters, including Unicode characters and escape sequences, correctly and efficiently.

The function should not modify the original string and should work with strings of any length. The output string should contain underscores in place of special characters, while non-special characters, including Unicode characters and escape sequences, should remain unchanged.
"""

import string

def special_to_underscore(input_str): 
    trans = str.maketrans(string.punctuation, '_'*len(string.punctuation))
    return input_str.translate(trans)