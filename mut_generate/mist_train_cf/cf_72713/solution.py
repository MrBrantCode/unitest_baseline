"""
QUESTION:
Construct a function named `prime_less_than` that takes a positive integer `n` and returns a list of prime numbers less than `n`. The function should handle cases where `n` is less than or equal to 1, in which case it should return an empty list.
"""

def prime_less_than(n):
    primes = []
    for possible_prime in range(2, n):
        is_prime = True
        for num in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_prime)
    return primes