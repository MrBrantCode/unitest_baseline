"""
QUESTION:
Write a function named `sum_of_primes_squared` that calculates the sum of the squares of all prime numbers within a given range, from 2 to n (inclusive), where n is 20. The function should return the total sum of these squared values.
"""

def sum_of_primes_squared(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    total_sum = 0
    for i in range(2, n + 1):
        if is_prime(i):
            total_sum += i ** 2
    return total_sum