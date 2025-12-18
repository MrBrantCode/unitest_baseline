"""
QUESTION:
Write a function `egcd(a, b)` that calculates the Extended Greatest Common Divisor (EGCD) of two given integers `a` and `b`. The function should return the GCD and the coefficients of Bézout's identity, which are integers `x` and `y` that satisfy `ax + by = gcd(a, b)`.
"""

def egcd(a, b):
    """
    Calculate the Extended Greatest Common Divisor (EGCD) of two given integers.
    
    Args:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    tuple: A tuple containing the GCD and the coefficients of Bézout's identity (x, y).
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)