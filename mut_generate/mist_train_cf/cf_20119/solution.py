"""
QUESTION:
Write a function `gcd(n1, n2)` that calculates the greatest common divisor of two integers `n1` and `n2` without using built-in Python functions or libraries for GCD calculation. The function should have a time complexity of O(log(min(n1, n2))) and a space complexity of O(1), and it should be able to handle both positive and negative input numbers.
"""

def gcd(n1, n2):
    """
    Calculate the greatest common divisor of two integers n1 and n2.
    
    The function uses the Euclidean algorithm and has a time complexity of O(log(min(n1, n2)))
    and a space complexity of O(1). It can handle both positive and negative input numbers.
    
    Parameters:
    n1 (int): The first integer.
    n2 (int): The second integer.
    
    Returns:
    int: The greatest common divisor of n1 and n2.
    """
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    if n1 < 0:
        n1 = -n1
    if n2 < 0:
        n2 = -n2

    while n2 != 0:
        remainder = n1 % n2
        n1 = n2
        n2 = remainder

    return n1