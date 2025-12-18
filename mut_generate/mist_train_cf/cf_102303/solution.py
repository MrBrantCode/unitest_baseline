"""
QUESTION:
Write a function `calculate_y` that takes four parameters: `x1`, `x2`, `x3`, and `n`, where `n` is a positive integer greater than 1. The function should calculate the value of `y` based on the formula `y = (x1^n + x2 + x3)(2x2 + 3x3)` and return the result. The time complexity of calculating `x1^n` should be O(n). Assume that the inputs are valid.
"""

def calculate_y(x1, x2, x3, n):
    """
    Calculate the value of y based on the formula y = (x1^n + x2 + x3)(2x2 + 3x3).

    Args:
        x1 (float): The base number.
        x2 (float): The second number.
        x3 (float): The third number.
        n (int): A positive integer greater than 1.

    Returns:
        float: The calculated value of y.
    """
    # Calculate x1^n with a time complexity of O(n) using a loop
    x1_power_n = 1
    for _ in range(n):
        x1_power_n *= x1
    
    # Calculate (x1^n + x2 + x3)
    sum_x = x1_power_n + x2 + x3
    
    # Calculate (2x2 + 3x3)
    sum_2x2_3x3 = 2 * x2 + 3 * x3
    
    # Multiply the results
    y = sum_x * sum_2x2_3x3
    
    return y