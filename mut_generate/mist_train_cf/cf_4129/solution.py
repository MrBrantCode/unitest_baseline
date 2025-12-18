"""
QUESTION:
Write a function `get_prime_factors(num, rng)` that finds all prime factors of a given integer `num` greater than 1, within a specified range `rng`. The function should handle cases where `num` or `rng` may be invalid (i.e., `num` may be less than or equal to 1, or `rng` may be less than or equal to 0). The function should return a list of prime factors found within the given range. 

Note: A prime factor is a prime number that can divide the given number without leaving a remainder.
"""

def get_prime_factors(num, rng):
    """
    Finds all prime factors of a given integer `num` greater than 1, within a specified range `rng`.
    
    Args:
    num (int): The number to find prime factors for.
    rng (int): The range within which to find prime factors.
    
    Returns:
    list: A list of prime factors found within the given range.
    """

    def is_prime(n):
        """Checks if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if num <= 1:
        return []
    prime_factors = []
    for i in range(2, rng+1):
        if num % i == 0 and is_prime(i):
            prime_factors.append(i)
    return prime_factors