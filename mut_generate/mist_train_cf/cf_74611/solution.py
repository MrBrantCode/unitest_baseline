"""
QUESTION:
Create a function called "add_prefix_suffix" that takes three parameters: the original string and the prefix and suffix to be added. The function should return the modified string with the added prefix and suffix without modifying the original string.
"""

def add_prefix_suffix(original_string, prefix, suffix):
    """
    This function adds a prefix and suffix to a given string without modifying the original string.
    
    Parameters:
    original_string (str): The original string.
    prefix (str): The prefix to be added to the original string.
    suffix (str): The suffix to be added to the original string.
    
    Returns:
    str: The modified string with the added prefix and suffix.
    """
    return prefix + original_string + suffix