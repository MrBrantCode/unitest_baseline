"""
QUESTION:
Write a function named `count_fragments` that takes a string as input and returns the number of fragments in the string. A fragment is defined as a sequence of consecutive characters separated by whitespace or punctuation. The function should ignore leading or trailing whitespace or punctuation, and consider punctuation characters such as '.', '!', and '?' as valid separators. The input string can contain any printable ASCII characters.
"""

import re

def count_fragments(input_string):
    """
    This function takes a string as input and returns the number of fragments in the string.
    A fragment is defined as a sequence of consecutive characters separated by whitespace or punctuation.
    
    Parameters:
    input_string (str): The input string to count fragments from.
    
    Returns:
    int: The number of fragments in the input string.
    """
    # Remove leading and trailing whitespace or punctuation
    input_string = input_string.strip(' .,!?;:')
    
    # Split the string into fragments using whitespace or punctuation as separators
    fragments = re.split(r'[ .,!?;:]+', input_string)
    
    # Return the number of fragments
    return len(fragments)