"""
QUESTION:
Implement a function `is_prime(n)` that determines whether an integer `n` is a prime number or not. The function should take into consideration odd and even numbers and utilize optimization strategies to improve efficiency. The input `n` will be a positive integer, and the function should return a boolean value indicating whether `n` is prime or not.
"""

def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True