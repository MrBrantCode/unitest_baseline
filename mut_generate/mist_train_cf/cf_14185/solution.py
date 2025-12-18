"""
QUESTION:
Write a function named `check_prime` that takes an integer as input and returns a boolean value indicating whether the number is prime or not, along with a list of all prime factors of the number if it is not prime. The function should consider a prime factor as a prime number that can divide the given number without leaving a remainder.
"""

import math

def check_prime(number):
    """
    Checks if a number is prime and returns its prime factors if it's not.

    Args:
    number (int): The number to check.

    Returns:
    tuple: A tuple containing a boolean indicating whether the number is prime and a list of its prime factors if it's not.
    """

    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False

        return True

    def prime_factors(num):
        factors = []

        for i in range(2, int(math.sqrt(num)) + 1):
            while num % i == 0:
                factors.append(i)
                num = num // i

        if num > 1:
            factors.append(num)

        return factors

    if is_prime(number):
        return True, []
    else:
        return False, prime_factors(number)