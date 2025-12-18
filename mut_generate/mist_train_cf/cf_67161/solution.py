"""
QUESTION:
Write a function `quote_string` that takes a string as input and returns the string with quotes around it. The function should be able to handle any string, including those with special characters or spaces. The output string should be a valid Python expression that could be used to recreate the original string.
"""

def quote_string(s):
    """
    This function takes a string as input and returns the string with quotes around it.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The string with quotes around it.
    """
    return repr(s)