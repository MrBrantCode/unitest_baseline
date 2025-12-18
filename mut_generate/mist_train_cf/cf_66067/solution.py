"""
QUESTION:
Write a function `gcdex(a, b)` that computes and returns the extended GCD of two integers `a` and `b` using a memory-efficient approach. The function should take two integers `a` and `b` as input, where 1 <= `a`, `b` <= 10^9, and return a tuple containing the GCD of `a` and `b` along with the coefficients of Bézout's identity.
"""

def gcdex(a: int, b: int) -> tuple:
    """
    Computes and returns the extended GCD of two integers `a` and `b` using a memory-efficient approach.

    Args:
    a (int): The first integer, where 1 <= `a` <= 10^9.
    b (int): The second integer, where 1 <= `b` <= 10^9.

    Returns:
    tuple: A tuple containing the GCD of `a` and `b` along with the coefficients of Bézout's identity.
    """
    if a == 0:
        return b, 0, 1
    gcd, x, y = gcdex(b % a, a)
    return gcd, y - (b // a) * x, x