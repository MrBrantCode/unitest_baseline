"""
QUESTION:
Write a function named `sum_first_n_primes` that calculates the sum of the first n prime numbers. The function should take an integer n as input and return the sum of the first n prime numbers.
"""

def sum_first_n_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = 0
    num = 2
    sum_primes = 0
    while prime_count < n:
        if is_prime(num):
            sum_primes += num
            prime_count += 1
        num += 1
    return sum_primes