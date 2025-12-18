"""
QUESTION:
Create a function `prime_index_elements` that takes a list of integers as input and returns a list of unique elements located at prime index positions. A prime index is a position in the list (1-indexed) that is a prime number. The function should handle edge cases and consider each element only once, even if it appears multiple times in the input list.
"""

def prime_index_elements(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    primes = set()
    for i in range(len(lst)):
        if is_prime(i + 1) and lst[i] not in primes:
            primes.add(lst[i])
    return list(primes)