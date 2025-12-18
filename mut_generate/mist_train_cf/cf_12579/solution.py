"""
QUESTION:
Write a function `is_prime(n)` that checks whether a number `n` is prime or not and use it to find the sum of all prime numbers between 1 and 100, excluding the number 2. The function should handle numbers greater than 1 and return a boolean value.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True