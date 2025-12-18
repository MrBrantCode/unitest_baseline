"""
QUESTION:
Create a function `is_multiply_prime(a)` that checks if the input number `a` is the product of exactly three unique prime integers. The input number `a` does not exceed 1000. Return `True` if the condition is met, and `False` otherwise.
"""

def is_multiply_prime(a):
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True   

    primes = [x for x in range(2, a) if is_prime(x)]
    factors = [x for x in primes if a % x == 0]
    unique_factors = len(set(factors))
    return len(primes) != 0 and unique_factors == 3