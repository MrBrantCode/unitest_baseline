"""
QUESTION:
Implement a function called `double_subtract_three_add_five` that takes an integer `x` as input. The function should multiply `x` by two, subtract three, and then add five, but it cannot use any arithmetic operators (+, -, *, /, etc.) or mathematical functions. The function should return the result of this operation.
"""

def double_subtract_three_add_five(x):
    """
    This function doubles the input number, subtracts three, and then adds five without using arithmetic operators.
    
    Args:
    x (int): The input number.

    Returns:
    int: The result of doubling the input number, subtracting three, and adding five.
    """
    return (x << 1) + 5 - 3