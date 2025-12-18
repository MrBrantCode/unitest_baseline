"""
QUESTION:
Write a function called `check_prime` that takes one argument, `number`, and returns a boolean value indicating whether the number is prime or not. The function should handle numbers up to 10^9. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. The function should iterate from 2 to the square root of the number (inclusive) and check if the number is divisible evenly by any of these values. If it is, the function should return False; otherwise, it should return True. 

Restrictions: The time complexity of the function should be O(sqrt(n)), where n is the input number.
"""

import math

def check_prime(number):
    """
    Check if a number is a prime number.

    Args:
    number -- the number to check

    Returns:
    True if the number is prime, False otherwise
    """
    if number <= 1:
        return False

    # Iterate from 2 to the square root of the number
    # The time complexity of this loop is O(sqrt(n))
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True