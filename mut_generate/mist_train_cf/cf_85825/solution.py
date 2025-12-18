"""
QUESTION:
Write a function `is_prime(n)` that takes an integer `n` as input. The function should return a tuple where the first element is a boolean indicating whether `n` is prime, and the second element is a list of divisors of `n` excluding 1 and `n` itself if `n` is not prime. If `n` is prime, the second element should be an empty list. The function should not return all divisors, only the first set it encounters. It should also assume that primes are positive integers greater than 1, and handle negative numbers and 0 accordingly.
"""

def entrance(n):
    """
    Returns a tuple where the first element is True if a given number is prime, False if not.
    If the number is not prime, the second element of the tuple is a list of its divisors excluding 1 and itself. 
    """
    if n < 2:
        return False, []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False, [i] + [n//i] 
    return True, []