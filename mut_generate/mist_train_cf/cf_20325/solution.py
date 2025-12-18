"""
QUESTION:
Write a function named `sum_of_primes` that takes two integers `start` and `end` as input and returns the sum of all prime numbers between `start` and `end` (inclusive).
"""

def sum_of_primes(start, end):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum