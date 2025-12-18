"""
QUESTION:
Write a function named `is_prime(num)` to check if a number is prime or not, and use it to print all prime numbers up to a given number `n` excluding numbers divisible by 5, and calculate and print the sum of these prime numbers and their total count. The input `n` is a positive integer. The function should return boolean values.
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