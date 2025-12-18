"""
QUESTION:
Write a recursive function `is_simple_power(x, n)` that determines if a number `x` is a simple power of `n` and returns the exponent. A simple power is defined as `n**k = x` where `k` is an integer. If `x` is not a simple power of `n`, return `False`. The function should not work for `n = 1`.
"""

def is_simple_power(x, n):
    """
    Determines if a number `x` is a simple power of `n` and returns the exponent.
    
    A simple power is defined as `n**k = x` where `k` is an integer.
    If `x` is not a simple power of `n`, return `False`.
    The function does not work for `n = 1`.
    """
    if n == 1:
        return False
    def power_test(x, n, k):
        if x == 1:
            return k
        elif x < 1:
            return False
        else:
            return power_test(x/n, n, k+1)
    return power_test(x, n, 0)