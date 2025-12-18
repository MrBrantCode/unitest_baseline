"""
QUESTION:
Write a function named `sum_first_n_primes` that takes an integer `n` as input and returns the sum of the first `n` prime numbers. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
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