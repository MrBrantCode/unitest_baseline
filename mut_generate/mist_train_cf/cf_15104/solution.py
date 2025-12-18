"""
QUESTION:
Write a function `sum_of_primes` that calculates the sum of all prime numbers between a given range, `start` and `end` (inclusive). The function should return the sum of all prime numbers in the given range.
"""

def sum_of_primes(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    prime_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum