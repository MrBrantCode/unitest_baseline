"""
QUESTION:
Write a function named `is_prime` that takes an integer as input and returns a boolean indicating whether the number is prime. Using this function, find the smallest prime number from a given list of distinct integers. The list can contain any number of integers, not necessarily eight. The function should return `None` if the list does not contain any prime numbers.
"""

def is_prime(num):
    """Check if a number is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True