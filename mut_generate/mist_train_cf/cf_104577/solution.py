"""
QUESTION:
Write a function named `switch` that takes an integer `x` as input and returns the corresponding string representation of the number (e.g. "Zero", "One", "Two", "Three", "Four", "Five") using a switch statement. The function should handle cases for `x` values ranging from 0 to 5 and return "Invalid number" for any other input.
"""

def switch(x):
    """
    Returns the string representation of the number.
    
    Args:
    x (int): The number to convert to string.
    
    Returns:
    str: The string representation of the number.
    """
    return {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five"
    }.get(x, "Invalid number")