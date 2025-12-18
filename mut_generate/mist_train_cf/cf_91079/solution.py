"""
QUESTION:
Write a function named `sum_of_primes` that calculates the sum of all prime numbers from 2 to a given input number `n`. The function should take an integer `n` as input and return the sum of all prime numbers in the range [2, n].
"""

def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes_sum = 0
    for i in range(2, n + 1):
        if is_prime(i):
            primes_sum += i
    return primes_sum