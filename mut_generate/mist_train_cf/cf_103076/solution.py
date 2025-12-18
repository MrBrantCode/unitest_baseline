"""
QUESTION:
Write a function named `swap_variables` that swaps the values of two variables without using a temporary variable. The function should have a time complexity of O(1) and should not use any built-in functions or libraries.
"""

def swap_variables(a, b):
    """
    Swaps the values of two variables without using a temporary variable.
    
    Time complexity: O(1)
    
    Parameters:
    a (int): The first variable to be swapped
    b (int): The second variable to be swapped
    
    Returns:
    tuple: A tuple containing the swapped values of a and b
    """
    a = a + b
    b = a - b
    a = a - b
    return a, b