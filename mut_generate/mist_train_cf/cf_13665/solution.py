"""
QUESTION:
Implement the function `is_prime(n)` to determine whether a given number is prime. The input `n` is a non-negative integer. The function should return `True` if the number is prime, and `False` otherwise. The solution must have a time complexity of O(n) and use constant space complexity, relying only on a few variables without any additional data structures. Built-in functions or libraries for mathematical operations are not allowed.
"""

def is_prime(n):
    """
    Determine whether a given number is prime.

    Args:
        n (int): A non-negative integer.

    Returns:
        bool: True if the number is prime, False otherwise.

    """
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True