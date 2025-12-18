"""
QUESTION:
Write a function named `boolean_operators` that demonstrates the functionality of three basic boolean operators: AND, OR, and NOT. The function should take three arguments: `x`, `y`, and `z`, and return the results of the following operations: (x > y AND x > z), (x > y OR x > z), and (NOT x > y). The function should use Python's built-in boolean operators `and`, `or`, and `not` to perform these operations.
"""

def boolean_operators(x, y, z):
    """
    This function demonstrates the functionality of three basic boolean operators: AND, OR, and NOT.
    
    Args:
        x (int): The first number to compare.
        y (int): The second number to compare.
        z (int): The third number to compare.
    
    Returns:
        tuple: A tuple containing the results of the operations (x > y AND x > z), (x > y OR x > z), and (NOT x > y).
    """
    and_operation = x > y and x > z
    or_operation = x > y or x > z
    not_operation = not (x > y)
    return and_operation, or_operation, not_operation