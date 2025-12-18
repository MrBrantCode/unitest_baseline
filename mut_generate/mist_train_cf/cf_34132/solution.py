"""
QUESTION:
Implement a function `trim_trailing_whitespace` that takes a list of strings as input and returns a list of strings with trailing whitespace removed from each string. Implement another function `compare_strings` that takes two lists of strings as input (the original list and the list processed by `trim_trailing_whitespace`) and returns a list of tuples containing the index of the differing strings and their respective original and processed versions.
"""

def trim_trailing_whitespace(strings):
    """
    Removes trailing whitespace from each string in the input list.
    
    Args:
    strings: A list of strings to be processed.
    
    Returns:
    A list of strings with trailing whitespace removed.
    """
    trimmed_strings = [s.rstrip() for s in strings]
    return trimmed_strings