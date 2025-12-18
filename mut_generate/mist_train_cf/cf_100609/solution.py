"""
QUESTION:
Generate a function `generate_primes(n)` that returns a list of the first `n` prime numbers. The function should be efficient in terms of runtime and memory usage. The function should also handle edge cases where `n` is a large value or the system's memory capacity is limited.
"""

def generate_primes(n):
    primes = []
    if n > 0:
        primes.append(2)
    if n > 1:
        primes.append(3)
    i = 5
    while len(primes) < n:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 2
    return primes