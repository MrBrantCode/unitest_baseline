"""
QUESTION:
Create a Python function named `is_prime(num)` that takes an integer `num` as input and returns a boolean value indicating whether the number is prime or not. Use this function to find the sum of all prime numbers between 1000 and 2000 (inclusive) and return the sum. The function should only check divisibility up to the square root of the number.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True