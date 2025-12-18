"""
QUESTION:
Write a function called `convert_to_camelcase` that takes a string as input, converts it to camelCase, and returns the result. The input string is in lowercase and contains underscores between words. The output should have the first word in lowercase and the first letter of each subsequent word capitalized.
"""

def convert_to_camelcase(s):
    """
    Converts a string from underscore notation to camelCase.
    
    Args:
        s (str): The input string in underscore notation.
    
    Returns:
        str: The input string converted to camelCase.
    """
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])