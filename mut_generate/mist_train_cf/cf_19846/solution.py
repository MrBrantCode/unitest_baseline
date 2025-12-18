"""
QUESTION:
Create a function `get_largest_prime(limit)` that returns the largest prime number from a list of prime numbers up to a given limit. The function should have a time complexity of O(n) and cannot use any external libraries or functions to check for prime numbers.
"""

def get_largest_prime(limit):
    primes = []
    is_prime_number = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime_number[p]:
            for i in range(p * p, limit + 1, p):
                is_prime_number[i] = False
        p += 1
    for p in range(2, limit + 1):
        if is_prime_number[p]:
            primes.append(p)
    return max(primes)