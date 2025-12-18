"""
QUESTION:
Create a function `filter_strings` that takes an array of strings as input and returns a list of strings where each string has a length greater than 5 and contains both uppercase and lowercase letters.
"""

def filter_strings(strings):
    """
    This function filters a list of strings and returns a list of strings 
    where each string has a length greater than 5 and contains both uppercase and lowercase letters.

    Args:
        strings (list): A list of strings

    Returns:
        list: A list of filtered strings
    """
    return [s for s in strings if len(s) > 5 and any(c.isupper() for c in s) and any(c.islower() for c in s)]