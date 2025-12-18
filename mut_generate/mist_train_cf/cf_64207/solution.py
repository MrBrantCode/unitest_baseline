"""
QUESTION:
Create a function called `split_string` that takes a string as input and returns a list of words. The function should split the string into words based on a specified delimiter. If no delimiter is provided, it should default to splitting on spaces.
"""

def split_string(s, delimiter=' '):
    """
    Splits a string into a list of words based on a specified delimiter.
    
    Args:
    s (str): The input string.
    delimiter (str): The delimiter to split the string by. Defaults to space.
    
    Returns:
    list: A list of words.
    """
    return s.split(delimiter)