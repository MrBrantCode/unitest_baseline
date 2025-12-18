"""
QUESTION:
Write a function `swap_case` that takes a string as input and returns a new string where all alphabetic characters are changed to the opposite case, while non-alphabetic characters remain unchanged.
"""

def swap_case(s):
    """
    Returns a new string where all alphabetic characters are changed to the opposite case,
    while non-alphabetic characters remain unchanged.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    str: The modified string.
    """
    return "".join(char.swapcase() for char in s)