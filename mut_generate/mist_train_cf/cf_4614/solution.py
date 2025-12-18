"""
QUESTION:
Write a function `sum_of_primes` that calculates the sum of all prime numbers between two given integers, `lower` (inclusive) and `upper` (inclusive). The function should return the sum of these prime numbers. The range of `lower` and `upper` is 1 to 2000.
"""

def sum_of_primes(lower, upper):
    """
    Calculate the sum of all prime numbers between two given integers, 
    lower (inclusive) and upper (inclusive).

    Args:
        lower (int): The lower bound of the range (inclusive).
        upper (int): The upper bound of the range (inclusive).

    Returns:
        int: The sum of all prime numbers in the range.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

    return sum(num for num in range(lower, upper + 1) if is_prime(num))