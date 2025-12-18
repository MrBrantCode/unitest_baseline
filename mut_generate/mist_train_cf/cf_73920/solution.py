"""
QUESTION:
Write a function `primes_in_range` that generates a list of prime numbers within a given range from `low` to `high` (inclusive), where `low` and `high` are integers. The function should return a list of integers representing the prime numbers in the range.
"""

def primes_in_range(low, high):
    """
    Generates a list of prime numbers within a given range from low to high (inclusive).

    Args:
        low (int): The lower bound of the range (inclusive).
        high (int): The upper bound of the range (inclusive).

    Returns:
        list: A list of integers representing the prime numbers in the range.
    """
    primes = []
    for num in range(low, high + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes