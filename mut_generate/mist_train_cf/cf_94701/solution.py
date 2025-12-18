"""
QUESTION:
Create a function `is_prime(n)` that checks if an integer `n` is a prime number without using built-in functions or libraries. Then, use this function to generate a list of prime numbers between 16 and 34 (inclusive). The function should return a list of integers. The prime checking algorithm should be implemented manually.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True