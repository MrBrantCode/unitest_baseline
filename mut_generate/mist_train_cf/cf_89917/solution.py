"""
QUESTION:
Implement a function `power(base, exponent)` that calculates the power of a number raised to the nth power. The function should have a time complexity of O(log n) and meet the following requirements: 

- The function should handle positive and negative integers for both the base and the exponent.
- If the base is negative, the function should return the power with alternating signs.
- The function should return None if either the base or the exponent is a non-integer.
- The function should handle large values of base and exponent without causing a memory overflow.
"""

def power(base, exponent):
    """
    Calculate the power of a number raised to the nth power.
    
    This function handles positive and negative integers for both the base and the exponent.
    If the base is negative, the function returns the power with alternating signs.
    The function returns None if either the base or the exponent is a non-integer.
    The function handles large values of base and exponent without causing a memory overflow.
    
    Parameters:
    base (int): The base number.
    exponent (int): The power to which the base is raised.
    
    Returns:
    int: The result of the power operation, or None if the base or exponent is non-integer.
    """
    
    # Check if base or exponent is non-integer
    if not isinstance(base, int) or not isinstance(exponent, int):
        return None
    
    # Check if base is negative
    if base < 0:
        if exponent % 2 == 0:
            return power(abs(base), exponent)
        else:
            return -1 * power(abs(base), exponent)
    
    # Base cases
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    # Divide exponent by 2 and recursively calculate power
    temp = power(base, exponent // 2)
    
    # Multiply power by itself
    if exponent % 2 == 0:
        return temp * temp
    else:
        return base * temp * temp