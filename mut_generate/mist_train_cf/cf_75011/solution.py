"""
QUESTION:
Create a function `match_english_alphabet` that takes a string as input and returns all the uppercase and lowercase English letters present in the string. The function should use a regular expression pattern to identify and match the letters.
"""

import re

def match_english_alphabet(input_string):
    """
    Returns all uppercase and lowercase English letters present in the input string.
    
    Args:
        input_string (str): The input string to find English letters.
    
    Returns:
        list: A list of all English letters found in the input string.
    """
    pattern = "[A-Za-z]"
    return re.findall(pattern, input_string)