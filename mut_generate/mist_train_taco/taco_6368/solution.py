"""
QUESTION:
Your task is to create a new implementation of `modpow` so that it computes `(x^y)%n` for large `y`. The problem with the current implementation is that the output of `Math.pow` is so large on our inputs that it won't fit in a 64-bit float.

You're also going to need to be efficient, because we'll be testing some pretty big numbers.
"""

def mod_pow(x, y, n):
    """
    Computes (x^y) % n efficiently for large values of y.

    Parameters:
    x (int): The base number.
    y (int): The exponent.
    n (int): The modulus.

    Returns:
    int: The result of (x^y) % n.
    """
    res = 1
    x = x % n
    while y > 0:
        if y & 1:
            res = res * x % n
        y >>= 1
        x = x * x % n
    return res