"""
QUESTION:
Create a function named `calculate_result` that takes three parameters: `a`, `b`, and `c`. The function should return the result of the operation on `b` and `c` based on the value of `a`: if `a` is 0, return `b * c`; if `a` is 1, return `b + c`; otherwise, return `b - c`. Implement this function using a switch-case structure.
"""

def calculate_result(a, b, c):
    """
    This function calculates the result of operation on b and c based on the value of a.
    
    Parameters:
    a (int): The operation to be performed (0: multiply, 1: add, else: subtract)
    b (int): The first operand
    c (int): The second operand
    
    Returns:
    int: The result of the operation
    """
    return {0: lambda x, y: x * y, 1: lambda x, y: x + y}.get(a, lambda x, y: x - y)(b, c)