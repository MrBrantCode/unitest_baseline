"""
QUESTION:
Write a Python function `calculate_y` that takes in four parameters: `x1`, `x2`, `x3`, and `n`, where `n` is a positive integer. Calculate the value of `y` using the formula `y = (x1^n + x2 + x3)(2x2 + 3x3)`. The function should return the calculated value of `y`. Assume that `x1`, `x2`, and `x3` are numeric values.
"""

def calculate_y(x1, x2, x3, n):
    """
    Calculate the value of y using the formula y = (x1^n + x2 + x3)(2x2 + 3x3).

    Parameters:
    x1 (numeric): The base value.
    x2 (numeric): The second value.
    x3 (numeric): The third value.
    n (int): The exponent. Must be a positive integer.

    Returns:
    numeric: The calculated value of y.
    """
    # Calculate x1^n
    x1_power_n = x1 ** n
    
    # Calculate (x1^n + x2 + x3)
    sum_x1_x2_x3 = x1_power_n + x2 + x3
    
    # Calculate (2x2 + 3x3)
    sum_2x2_3x3 = 2 * x2 + 3 * x3
    
    # Multiply the results
    y = sum_x1_x2_x3 * sum_2x2_3x3
    
    return y