"""
QUESTION:
Write a function `is_prime(n, i=2)` that determines whether a given integer `n` is a prime number or not using recursion. The function should have constant space complexity, a time complexity of O(sqrt(n)), and cannot use any additional data structures or built-in functions for mathematical operations. The function should return `True` if `n` is prime and `False` otherwise.
"""

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i*i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i+1)