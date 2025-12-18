"""
QUESTION:
Write a function `is_prime` to determine whether a given integer `n` is a prime number or not, using an iterative solution, constant space complexity, and a time complexity of O(sqrt(n)). You are not allowed to use any built-in functions or libraries for mathematical operations. The function should return `True` if `n` is a prime number and `False` otherwise.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True