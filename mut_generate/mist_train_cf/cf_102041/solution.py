"""
QUESTION:
Create a function `gcd(a, b)` that takes two positive integers `a` and `b` as input, where 1 ≤ a ≤ 10^6 and 1 ≤ b ≤ 10^6, and returns their greatest common divisor using the Euclidean algorithm. The function should have a time complexity of O(log min(a, b)).
"""

def gcd(a, b):
    """
    This function calculates the greatest common divisor of two positive integers a and b using the Euclidean algorithm.
    
    Parameters:
    a (int): The first positive integer.
    b (int): The second positive integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a