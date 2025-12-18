"""
QUESTION:
Write a function `reverse_alphanumeric` that takes an input string and returns a string containing only the alphanumeric characters from the input string in reverse order. The function should exclude all non-alphanumeric characters from the input string.
"""

import re

def reverse_alphanumeric(input_str):
    # Remove all non-alphanumeric characters
    alphanumeric_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)
    
    # Reverse the alphanumeric string
    reversed_str = alphanumeric_str[::-1]
    
    return reversed_str