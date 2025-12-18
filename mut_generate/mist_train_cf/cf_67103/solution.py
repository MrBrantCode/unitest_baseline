"""
QUESTION:
Compute the sum of all prime numbers within a given range. Define a function `aggregate_primes(start, end)` that calculates this sum for a specified range from `start` to `end` (inclusive). The function should return the sum of all prime numbers within this range.
"""

def aggregate_primes(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while (i * i) <= n:
            if (n % i == 0) or (n % (i + 2) == 0):
                return False
            i += 6
        return True

    aggregate = 0
    for num in range(start, end + 1):
        if is_prime(num):
            aggregate += num
    return aggregate