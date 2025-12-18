"""
QUESTION:
Create a function `is_perfect_prime` that takes a positive integer `n` as input and returns `True` if `n` is a perfect prime and `False` otherwise. A perfect prime is a prime number that is equal to the sum of all its divisors, including 1 and itself. The function should use a helper function `get_divisors` that returns a list of all the divisors of a given number `n` with a time complexity of O(n).
"""

def get_divisors(n):
    """Return a list of all divisors of a given number n"""
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_perfect_prime(n):
    """Check if a given number n is a perfect prime."""
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    divisors = get_divisors(n)
    divisor_sum = sum(divisors)

    return divisor_sum == n