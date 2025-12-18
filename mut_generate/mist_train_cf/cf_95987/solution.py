"""
QUESTION:
Implement a function `power(base, exponent)` that calculates the result of the power operation using a recursive approach. The function should have a time complexity of O(log n) where n is the exponent number. It should handle negative exponents and return a float if necessary. The function should not use the built-in power function or any external libraries.
"""

def power(base, exponent):
    """
    Calculate the result of the power operation using a recursive approach.

    Args:
        base (float): The base number.
        exponent (int): The exponent number.

    Returns:
        float: The result of the power operation.

    Time Complexity:
        O(log n) where n is the exponent number.
    """
    if exponent == 0:
        return 1
    
    if exponent < 0:
        return 1 / power(base, -exponent)
    
    if exponent % 2 == 0:
        return power(base * base, exponent // 2)
    
    return base * power(base * base, (exponent - 1) // 2)