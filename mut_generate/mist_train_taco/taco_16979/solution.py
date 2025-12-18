"""
QUESTION:
It's March and you just can't seem to get your mind off brackets. However, it is not due to basketball. You need to extract statements within strings that are contained within brackets.

You have to write a function that returns a list of statements that are contained within brackets given a string. If the value entered in the function is not a string, well, you know where that variable should be sitting.

Good luck!
"""

import re

def extract_statements_in_brackets(input_string):
    """
    Extracts statements within brackets from the given input string.

    Parameters:
    input_string (str): The string from which to extract statements within brackets.

    Returns:
    list: A list of statements contained within brackets if input_string is a string.
    str: 'Take a seat on the bench.' if input_string is not a string.
    """
    REGEX = re.compile(r'\[(.*?)\]')
    
    if not isinstance(input_string, str):
        return 'Take a seat on the bench.'
    
    return REGEX.findall(input_string)