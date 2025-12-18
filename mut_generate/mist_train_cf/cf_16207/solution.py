"""
QUESTION:
Write a function `sum_of_primes` that calculates the sum of all prime numbers from 1 to a given number n. The function should return the sum of all prime numbers within the range. The given number n is assumed to be a positive integer. The function should not take any arguments other than n.
"""

def sum_of_primes(n):
    """
    This function calculates the sum of all prime numbers from 1 to a given number n.

    Args:
        n (int): A positive integer.

    Returns:
        int: The sum of all prime numbers within the range.
    """
    total_sum = 0
    for num in range(1, n + 1):
        is_prime = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and num != 1:
            total_sum += num
    return total_sum