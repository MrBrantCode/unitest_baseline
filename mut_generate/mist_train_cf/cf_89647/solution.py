"""
QUESTION:
Write a function `is_prime(n, i=2)` that determines whether a given integer `n` is a prime number or not using a recursive solution. The function should have a time complexity of O(sqrt(n)) and use constant space complexity. It should not use any additional data structures besides a few variables, nor any built-in functions or libraries for mathematical operations.
"""

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i*i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i+1)