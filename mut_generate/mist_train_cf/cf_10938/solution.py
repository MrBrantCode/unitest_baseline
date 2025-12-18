"""
QUESTION:
Write a Python function named `is_empty` that takes a string as input and returns `True` if the string is empty after ignoring leading and trailing whitespace characters, and `False` otherwise. The function should handle cases where the string contains only whitespace characters.
"""

def is_empty(string):
    """
    Returns True if the input string is empty after ignoring leading and trailing whitespace characters, False otherwise.
    
    Parameters:
    string (str): The input string to be checked.
    
    Returns:
    bool: True if the string is empty, False otherwise.
    """
    # Remove leading and trailing whitespace characters and check if the string is empty
    return len(string.strip()) == 0