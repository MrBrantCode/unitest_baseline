"""
QUESTION:
Write a function `sum_of_primes(n)` that calculates the sum of all prime numbers less than the given number `n`. Assume `n` is a positive integer. The function should return the sum of prime numbers as an integer.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    prime_sum = 0
    for i in range(2, n):
        if is_prime(i):
            prime_sum += i
    return prime_sum