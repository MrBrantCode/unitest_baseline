"""
QUESTION:
Design a function named `lcm(a, b, c)` that calculates the least common multiple of three positive 32-bit signed integers `a`, `b`, and `c`. The function should take into account the range of 32-bit signed integer values.
"""

def lcm(a, b, c):
    """
    This function calculates the least common multiple (LCM) of three positive 32-bit signed integers a, b, and c.
    
    Parameters:
    a (int): The first positive 32-bit signed integer.
    b (int): The second positive 32-bit signed integer.
    c (int): The third positive 32-bit signed integer.
    
    Returns:
    int: The least common multiple of a, b, and c.
    """
    
    def gcd(x, y):
        # calculate GCD
        while (y):
            x, y = y, x % y
        return x
    
    # calculate LCM
    temp = a * b // gcd(a, b)
    return temp * c // gcd(temp, c)