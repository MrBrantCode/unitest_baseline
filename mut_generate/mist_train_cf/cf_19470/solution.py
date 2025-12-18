"""
QUESTION:
Implement a function called `find_first_match` that takes in two arguments: a string `text` and a string `pattern`. The function should return the position (index) of the first occurrence of the `pattern` in the `text`. If the `pattern` is not found, the function should return -1.
"""

def find_first_match(text, pattern):
    """
    This function finds the position of the first occurrence of a pattern in a given text.
    
    Parameters:
    text (str): The string in which the pattern is to be found.
    pattern (str): The pattern to be found in the text.
    
    Returns:
    int: The index of the first occurrence of the pattern. Returns -1 if the pattern is not found.
    """
    try:
        return text.index(pattern)
    except ValueError:
        return -1