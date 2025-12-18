"""
QUESTION:
Write a function named `largestPrimeFactorSieve` that takes an integer `n` as input and returns the largest prime factor of `n`. The function should iteratively divide `n` by the smallest prime factor until `n` is reduced to 1, and keep track of the largest prime factor found. The function should be efficient for large inputs by only iterating up to the square root of `n`.
"""

def largestPrimeFactorSieve(n):
    """
    This function finds the largest prime factor of a given number 'n'.
    
    Args:
        n (int): The input number.

    Returns:
        int: The largest prime factor of 'n'.
    """
    largestPrime = -1

    # Divide by 2 until n becomes odd
    while n % 2 == 0:
        largestPrime = 2
        n >>= 1

    # n must be odd now, so finding the largest prime factor starting from 3 to the square root of n
    i = 3
    while i * i <= n:
        if n % i == 0:
            largestPrime = i
            n = n / i
        else:
            i += 2

    # If n is still a prime number and greater than 2, then n will be the largest prime factor
    if n > 2:
        largestPrime = n

    return largestPrime