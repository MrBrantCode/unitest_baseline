"""
QUESTION:
Write a function `check_prime_number` that takes an integer `number` as input and returns `True` if the number is a prime number within the range of 10,000 to 20,000 and is divisible by both 3 and 5, and `False` otherwise. The function should not use any built-in prime number checking functions or libraries and should have a time complexity of O(n^(1/2)) and a space complexity of O(1).
"""

import math

def check_prime_number(number):
    """
    Checks if the number is a prime number within the range of 10,000 to 20,000 and is divisible by both 3 and 5.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a prime number within the range and is divisible by both 3 and 5, False otherwise.
    """
    # Check if the number is within the range of 10,000 to 20,000
    if not (number >= 10000 and number <= 20000):
        return False

    # Check if the number is divisible by both 3 and 5
    if number % 3 != 0 or number % 5 != 0:
        return False

    # Check if the number is a prime number
    if number < 2:  # 0, 1, and negative numbers are not prime
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True