"""
QUESTION:
Create a function `count_distinct_primes_sum(N)` that takes a positive integer `N` as input and returns two values: the count of distinct prime numbers less than or equal to `N` and the sum of those prime numbers. The function should consider prime numbers in the range from 2 to `N` (inclusive) and the prime numbers should be distinct.
"""

def count_distinct_primes_sum(N):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = set()
    prime_sum = 0
    for num in range(2, N + 1):
        if is_prime(num):
            primes.add(num)
            prime_sum += num
    return len(primes), prime_sum