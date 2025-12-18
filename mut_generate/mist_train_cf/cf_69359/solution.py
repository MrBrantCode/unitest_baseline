"""
QUESTION:
Implement a function named `count_up_to(n)` that takes a non-negative whole number `n` as input and returns a list of prime numbers smaller than `n`. The function should not include `n` in the list.
"""

def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [x for x in range(2, n) if is_prime(x)]
    return primes