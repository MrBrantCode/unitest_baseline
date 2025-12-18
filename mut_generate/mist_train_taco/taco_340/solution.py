"""
QUESTION:
Create a program that will take in a string as input and, if there are duplicates of more than two alphabetical characters in the string, returns the string with all the extra characters in a bracket.

For example, the input "aaaabbcdefffffffg" should return  "aa[aa]bbcdeff[fffff]g" 

Please also ensure that the input is a string, and return "Please enter a valid string" if it is not.
"""

import re

def parse_string_with_duplicates(input_string):
    """
    Processes the input string by wrapping duplicates of more than two alphabetical characters in brackets.

    Parameters:
    input_string (str): The string to be processed.

    Returns:
    str: The processed string with duplicates wrapped in brackets, or "Please enter a valid string" if the input is not a valid string.
    """
    if not isinstance(input_string, str):
        return "Please enter a valid string"
    
    return re.sub('(.)\\1(\\1+)', '\\1\\1[\\2]', input_string)