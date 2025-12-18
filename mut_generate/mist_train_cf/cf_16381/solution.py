"""
QUESTION:
Write a function `is_prime(num)` that takes an integer `num` as input and returns `True` if it is a prime number, otherwise returns `False`. Then, write a program that uses a loop to find all prime numbers up to a given number `n`, skipping any numbers divisible by 5, calculates and prints the sum of these prime numbers, and counts and prints the total number of these prime numbers. Assume the input number `n` is provided.
"""

def is_prime(num):
    """
    Checks if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True