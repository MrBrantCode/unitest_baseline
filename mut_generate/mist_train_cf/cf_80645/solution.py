"""
QUESTION:
Write a function, `find_even_primes`, that finds and returns all even prime numbers up to a given limit. The function should take an integer `limit` as input and return a list of even prime numbers less than or equal to the limit. The function should also return the count of even prime numbers found.
"""

def find_even_primes(limit):
    """
    Finds and returns all even prime numbers up to a given limit.

    Args:
    limit (int): The upper limit for finding even prime numbers.

    Returns:
    list: A list of even prime numbers less than or equal to the limit.
    int: The count of even prime numbers found.
    """
    def is_prime(n):
        """Returns True if given non-negative integer is prime, otherwise returns False"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    even_primes = [n for n in range(limit + 1) if n % 2 == 0 and is_prime(n)]
    return even_primes, len(even_primes)