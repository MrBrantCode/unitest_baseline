"""
QUESTION:
Create a function called `strip_inner_whitespace` that takes a string as input, removes any leading or trailing whitespace characters, but leaves inner whitespace characters intact, and then returns the modified string.
"""

def strip_inner_whitespace(my_string):
    """
    This function takes a string as input, removes any leading or trailing whitespace characters, 
    but leaves inner whitespace characters intact, and then returns the modified string.
    
    Parameters:
    my_string (str): The input string to be modified
    
    Returns:
    str: The modified string with leading and trailing whitespace characters removed
    """
    return my_string.strip()