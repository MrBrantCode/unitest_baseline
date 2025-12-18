"""
QUESTION:
Write a function named `is_prime` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number or not. Then, use this function to find all prime numbers in a given nested list and print them. The function should be able to handle integers less than 2, which are not prime.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True