"""
QUESTION:
Write a function called largest_prime_factor that finds the largest prime factor of a given number n that is greater than a certain threshold. The function should take two parameters: n and threshold. It should return the largest prime factor of n that is greater than the threshold.
"""

def largest_prime_factor(n, threshold):
    """
    This function finds the largest prime factor of a given number n that is greater than a certain threshold.

    Parameters:
    n (int): The number to find the largest prime factor of.
    threshold (int): The minimum value of the prime factor.

    Returns:
    int: The largest prime factor of n that is greater than the threshold.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(n, threshold, -1):
        if n % i == 0 and is_prime(i):
            return i
    return None