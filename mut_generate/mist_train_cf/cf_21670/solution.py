"""
QUESTION:
Write a function `f(x)` to calculate the value of the polynomial $x(x + 1)(x + 5) + 6$ using recursion, where the base case is `f(0) = 6`.
"""

def f(x):
    """
    Calculate the value of the polynomial x(x + 1)(x + 5) + 6 using recursion.
    
    Args:
    x (int): The input value.
    
    Returns:
    int: The value of the polynomial.
    """
    # Base case
    if x == 0:
        return 6
    # Recursive case
    else:
        return x * (x + 1) * (x + 5) + 6