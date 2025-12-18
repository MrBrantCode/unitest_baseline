"""
QUESTION:
Create a generic function that adds two values of different data types in Swift, such as Int, Double, String, and Float, without requiring explicit type extensions for each data type. The function should work with any data type that supports the addition operation.
"""

def add_values(a, b):
    """
    A generic function that adds two values of different data types.
    
    Args:
        a (int, float, str): The first value to add.
        b (int, float, str): The second value to add.
    
    Returns:
        The result of adding a and b.
    """
    return a + b