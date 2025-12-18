"""
QUESTION:
Create a function `is_prime(n)` that determines whether a given positive integer `n` is a safe prime number. A safe prime number is a prime number of the form `2p + 1`, where `p` itself is also a prime number. The function should return `True` for safe prime numbers and `False` otherwise.
"""

def is_prime(n):
    """Returns true for safe prime integers, false for non-safe prime integers."""
    def is_prime_helper(num):
        """Returns true for prime integers, false for non-prime integers."""
        if num <= 1 or (num % 2 == 0 and num > 2): 
            return False
        return all(num % i for i in range(3, int(num**0.5) + 1, 2))

    if n <= 2:
        return False
    if n % 2 == 1 and is_prime_helper(n):
        p = (n - 1) / 2
        return is_prime_helper(p)
    return False