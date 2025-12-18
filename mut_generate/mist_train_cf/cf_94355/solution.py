"""
QUESTION:
Write a function named `is_prime` that takes a single integer `n` as input and returns a boolean value indicating whether `n` is a prime number or not. Do not use any built-in functions or libraries to check for prime numbers. Implement the prime-checking logic from scratch using only basic programming constructs, and ensure the function has a time complexity of O(sqrt(n)).
"""

def entrance(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True