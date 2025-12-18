"""
QUESTION:
Create a function `check_input` that takes one parameter `n`. The function should return "Hey I'm a string" if `n` is a string, "Hey I'm not here" if `n` is a negative number, and "Hey I'm a positive number" otherwise. The function should handle cases where `n` is a string, an integer, or any other type of input.
"""

def check_input(n):
    """
    This function checks the type and value of the input.
    
    Args:
    n: The input to be checked.
    
    Returns:
    A string indicating whether the input is a string, a negative number, or a positive number.
    """
    # check if n is a string
    if isinstance(n, str):
        return "Hey I'm a string"
    
    # check if n is an integer
    elif isinstance(n, int):
        # check if n is negative
        if n < 0:
            return "Hey I'm not here"
        else:
            return "Hey I'm a positive number"
    
    # if n is neither a string nor an integer, return a default message
    else:
        return "Invalid input"