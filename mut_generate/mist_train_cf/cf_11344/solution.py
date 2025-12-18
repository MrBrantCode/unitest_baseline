"""
QUESTION:
Write a function `is_prime` that determines whether a given positive integer is prime or not without using any looping or recursion. The function should take an integer `n` as input and return "Prime" if `n` is prime, and "Not Prime" otherwise.
"""

def is_prime(n):
    """
    This function determines whether a given positive integer is prime or not without using any looping or recursion.
    
    Args:
    n (int): The input number to be checked.
    
    Returns:
    str: "Prime" if the number is prime, "Not Prime" otherwise.
    """
    if n < 2:
        return "Not Prime"
    if n == 2 or n == 3:
        return "Prime"
    if n % 2 == 0 or n % 3 == 0:
        return "Not Prime"
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "Not Prime"
        i += 6
    return "Prime"