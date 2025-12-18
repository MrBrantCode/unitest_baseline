"""
QUESTION:
Create a function `is_prime` that takes an integer as input and returns a boolean indicating whether the number is prime or not. Then, create a list of prime numbers from a given list of integers by filtering out non-prime numbers using the `is_prime` function and sort the resulting list in descending order.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True