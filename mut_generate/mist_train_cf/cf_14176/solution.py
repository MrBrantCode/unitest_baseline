"""
QUESTION:
Write a function `sum_of_primes(n)` that calculates the sum of all prime numbers between 1 and `n`, where `n` is a given integer. The function should return the sum of these prime numbers.
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
    for num in range(2, n+1):
        if is_prime(num):
            primes_sum += num
    return primes_sum