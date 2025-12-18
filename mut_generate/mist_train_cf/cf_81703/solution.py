"""
QUESTION:
Write a function called `find_max` that takes two parameters and returns the maximum value if both parameters are either integers or floats. If either parameter is not a number, the function should return "Invalid inputs".
"""

def find_max(x, y):
    """
    This function finds the maximum value between two parameters.
    
    Args:
    x (int or float): The first number to compare.
    y (int or float): The second number to compare.
    
    Returns:
    max(x, y) if both x and y are numbers, "Invalid inputs" otherwise.
    """
    return max(x, y) if isinstance(x, (int, float)) and isinstance(y, (int, float)) else "Invalid inputs"