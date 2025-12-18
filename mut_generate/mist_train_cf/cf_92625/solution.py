"""
QUESTION:
Write a function `is_prime(n)` to check if a number `n` is prime and another function `sum_of_primes(a, b)` to find the sum of all prime numbers between `a` and `b` (inclusive), where `1 <= a <= b <= 1000`.
"""

def sum_of_primes(a, b):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    sum_of_primes = 0
    for num in range(a, b + 1):
        if is_prime(num):
            sum_of_primes += num
    return sum_of_primes