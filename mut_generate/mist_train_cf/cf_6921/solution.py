"""
QUESTION:
Write a function `count_primes(n)` that returns the count of all prime numbers from 1 to `n` (inclusive) where `n` is a positive integer greater than or equal to 2. Do not use any built-in prime number libraries or mathematical operations/formulas related to prime numbers.
"""

def count_primes(n):
    count = 0

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for current_num in range(2, n + 1):
        if is_prime(current_num):
            count += 1

    return count