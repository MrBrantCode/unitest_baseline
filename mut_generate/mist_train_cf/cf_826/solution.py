"""
QUESTION:
Write a function `sum_primes(n)` that calculates the sum of all prime numbers from 1 to a given number `n` (inclusive). The function should have a time complexity of O(n^2) and a space complexity of O(n).
"""

def sum_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return sum(primes)