"""
QUESTION:
Write a function called `is_prime(n)` that checks whether a given number `n` is prime or not. If `n` is prime, the function should return `True` and an empty list. If `n` is not prime, the function should return `False` and a list of its divisors. The function should handle integers greater than or equal to 1.
"""

def is_prime(n):
    """ Returns True if a given number is prime. False if not.
    If the number is not prime, returns also a list of its divisors.
    """
    if n < 2:
        return False, []
    divisors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.extend([i, n // i])
            for j in range(i+1, n // i):
                if n % j == 0:
                    divisors.extend([j, n // j])
    if divisors:
        return False, sorted(set(divisors))
    return True, []