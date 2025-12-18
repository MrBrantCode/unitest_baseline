"""
QUESTION:
Write a function named `prime_divisor_pairs` that takes an integer `n` as input and returns a list of tuples in the form (x, n/x) where x is a prime number that divides n. The list should only include pairs where x is a prime number.
"""

def prime_divisor_pairs(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    pairs = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
            pairs.append((i, n // i))
        if n % i == 0 and is_prime(n // i):
            pairs.append((n // i, i))
    if is_prime(n):
        pairs.append((n, 1))
    return list(set(pairs))